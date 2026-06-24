"""
E2 - Simulated user-survey data generator.

Generates n=52 simulated respondents answering a 24-item, 8-construct
questionnaire on a 5-point Likert scale. Responses are produced from a latent
structural model that mirrors the proposed research model:

    Trust        <- SQ, PE, PS, EM, (-)PR
    Satisfaction <- SQ, PE, PS, EM, (-)PR
    Loyalty      <- Trust, Satisfaction

Each construct has 3 observed items = latent score + item noise, mapped to a
1..5 Likert scale. This is SIMULATED pilot data for prototype evaluation
(instructor's checklist permits reasonable simulated data); it is NOT collected
from real respondents and is labelled as such in the paper.

Output: data/survey_responses.csv  (wide format, one row per respondent)
"""
import numpy as np
import pandas as pd
from pathlib import Path

RNG = np.random.default_rng(7)
N = 52
OUT = Path(__file__).resolve().parents[1] / "data" / "survey_responses.csv"

# Exogenous latent constructs (standardized ~ N(0,1)), mildly inter-correlated.
def corr_normal(n, base):
    return 0.45 * base + np.sqrt(1 - 0.45**2) * RNG.normal(0, 1, n)

shared = RNG.normal(0, 1, N)          # general "good experience" factor
SQ = corr_normal(N, shared)           # service quality
PE = corr_normal(N, shared)           # personalization
PS = corr_normal(N, shared)           # problem solving
EM = corr_normal(N, shared)           # perceived empathy
PR = RNG.normal(0, 1, N)              # privacy risk (independent-ish)

# Structural equations (standardized betas + disturbance).
TR = 0.34*SQ + 0.20*PE + 0.22*PS + 0.18*EM - 0.21*PR + RNG.normal(0, 0.55, N)
SA = 0.30*SQ + 0.24*PE + 0.26*PS + 0.15*EM - 0.17*PR + RNG.normal(0, 0.55, N)
LI = 0.46*TR + 0.38*SA + RNG.normal(0, 0.55, N)

latents = {"SQ": SQ, "PE": PE, "PS": PS, "EM": EM, "PR": PR,
           "TR": TR, "SA": SA, "LI": LI}

# Map a standardized latent to a 1..5 Likert item with item-specific noise.
def to_likert(latent, item_noise=0.45, mean=3.7, spread=0.85):
    val = mean + spread * (latent + RNG.normal(0, item_noise, len(latent)))
    return np.clip(np.round(val), 1, 5).astype(int)

# Construct means tuned so quality constructs skew positive, privacy risk neutral.
means = {"SQ": 3.9, "PE": 3.6, "PS": 3.8, "EM": 3.7,
         "PR": 3.0, "TR": 3.8, "SA": 3.9, "LI": 3.8}

cols = {}
for c, lat in latents.items():
    for i in (1, 2, 3):
        cols[f"{c}{i}"] = to_likert(lat, mean=means[c])

# Demographics
cols["age"] = RNG.integers(18, 26, N)
cols["gender"] = RNG.choice(["Male", "Female"], N, p=[0.55, 0.45])
cols["prior_chatbot_use"] = RNG.choice(
    ["Never", "Sometimes", "Often"], N, p=[0.25, 0.5, 0.25])

df = pd.DataFrame(cols)
df.insert(0, "respondent_id", np.arange(1, N + 1))
OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT, index=False)
print(f"Wrote {len(df)} respondents -> {OUT}")
print(df.head().to_string(index=False))
