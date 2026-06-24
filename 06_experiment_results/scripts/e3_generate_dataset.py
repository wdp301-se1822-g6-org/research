"""
E3 - Synthetic customer dataset generator.

Generates a simulated customer-behavior dataset for the loyalty-retention
prediction experiment. All data is SYNTHETIC and intended for prototype
evaluation only (the instructor's checklist explicitly permits reasonable
simulated data). The retention label is generated from a known logistic
data-generating process plus Gaussian noise, so a well-specified classifier
should be able to recover the signal but not perfectly (noise floor enforced).

Output: data/customers.csv
"""
import numpy as np
import pandas as pd
from pathlib import Path

RNG = np.random.default_rng(42)
N = 1000
OUT = Path(__file__).resolve().parents[1] / "data" / "customers.csv"

tiers = np.array(["Bronze", "Silver", "Gold", "Platinum"])
tier_probs = np.array([0.40, 0.30, 0.20, 0.10])
tier_idx = RNG.choice(len(tiers), size=N, p=tier_probs)
tier_rank = tier_idx.astype(float)  # 0..3, higher = better tier

num_interactions = RNG.poisson(15, N)
purchase_freq = RNG.gamma(2.0, 1.5, N)                 # purchases / month
loyalty_points = np.clip(RNG.normal(500, 200, N) + tier_rank * 150, 0, None)
chatbot_usage = RNG.poisson(5, N)
avg_satisfaction = RNG.beta(5, 2, N) * 5               # 0..5
avg_trust = RNG.beta(4, 2, N) * 5                      # 0..5
complaints_3m = RNG.poisson(1, N)
days_since_active = RNG.exponential(30, N)

# --- Known data-generating process for the retention label ---
# Standardize drivers, combine into a latent score, pass through logistic.
def z(x):
    return (x - x.mean()) / (x.std() + 1e-9)

latent = (
    0.9 * z(avg_satisfaction)
    + 0.8 * z(avg_trust)
    + 0.6 * z(purchase_freq)
    + 0.5 * z(chatbot_usage)
    + 0.4 * z(loyalty_points)
    + 0.3 * tier_rank
    - 0.7 * z(complaints_3m)
    - 0.9 * z(days_since_active)
)
# Add irreducible noise so the problem is not trivially separable.
latent_noisy = latent + RNG.normal(0, 1.1, N)
# Shift intercept to target ~68/32 retain/churn imbalance.
prob_retain = 1 / (1 + np.exp(-(latent_noisy + 0.85)))
will_retain = (RNG.uniform(0, 1, N) < prob_retain).astype(int)

df = pd.DataFrame({
    "customer_id": np.arange(1, N + 1),
    "num_interactions": num_interactions,
    "purchase_freq_per_month": purchase_freq.round(2),
    "loyalty_points": loyalty_points.round(0).astype(int),
    "current_tier": tiers[tier_idx],
    "tier_rank": tier_rank.astype(int),
    "chatbot_usage_freq": chatbot_usage,
    "avg_satisfaction_score": avg_satisfaction.round(2),
    "avg_trust_score": avg_trust.round(2),
    "complaint_count_3m": complaints_3m,
    "days_since_last_active": days_since_active.round(1),
    "will_retain_next_6m": will_retain,
})

OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT, index=False)
print(f"Wrote {len(df)} rows -> {OUT}")
print("Retention rate: %.3f" % df["will_retain_next_6m"].mean())
print(df.head())
