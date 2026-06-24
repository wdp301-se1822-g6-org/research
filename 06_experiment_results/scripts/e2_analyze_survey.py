"""
E2 - Survey analysis: reliability, descriptives, correlation, regression.

Reads data/survey_responses.csv and produces:
  - Construct scores (mean of 3 items each)
  - Cronbach's alpha per construct (reliability, target >= 0.70)
  - Descriptive statistics (mean, SD) per construct
  - Pearson correlation matrix among constructs (+ heatmap figure)
  - Three OLS regressions matching the research model:
        Trust        ~ SQ + PE + PS + EM + PR
        Satisfaction ~ SQ + PE + PS + EM + PR
        Loyalty      ~ Trust + Satisfaction

Outputs:
  tables/e2_reliability_descriptives.csv
  tables/e2_correlation_matrix.csv
  tables/e2_regression_results.csv
  figures/e2_correlation_heatmap.png
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE / "data" / "survey_responses.csv")

CONSTRUCTS = {
    "Service Quality": ["SQ1", "SQ2", "SQ3"],
    "Personalization": ["PE1", "PE2", "PE3"],
    "Problem Solving": ["PS1", "PS2", "PS3"],
    "Perceived Empathy": ["EM1", "EM2", "EM3"],
    "Privacy Risk": ["PR1", "PR2", "PR3"],
    "Trust": ["TR1", "TR2", "TR3"],
    "Satisfaction": ["SA1", "SA2", "SA3"],
    "Loyalty Intention": ["LI1", "LI2", "LI3"],
}

def cronbach_alpha(items_df):
    k = items_df.shape[1]
    item_var = items_df.var(axis=0, ddof=1).sum()
    total_var = items_df.sum(axis=1).var(ddof=1)
    return (k / (k - 1)) * (1 - item_var / total_var)

# --- Reliability + descriptives ---
rows, scores = [], {}
for name, items in CONSTRUCTS.items():
    sub = df[items]
    score = sub.mean(axis=1)
    scores[name] = score
    rows.append({
        "Construct": name,
        "Items": len(items),
        "Mean": round(score.mean(), 3),
        "SD": round(score.std(ddof=1), 3),
        "Cronbach_alpha": round(cronbach_alpha(sub), 3),
    })
rel = pd.DataFrame(rows)
rel.to_csv(BASE / "tables" / "e2_reliability_descriptives.csv", index=False)
print("=== Reliability & Descriptives (n=%d) ===" % len(df))
print(rel.to_string(index=False))

scores_df = pd.DataFrame(scores)

# --- Correlation matrix ---
corr = scores_df.corr(method="pearson").round(3)
corr.to_csv(BASE / "tables" / "e2_correlation_matrix.csv")
print("\n=== Pearson Correlation Matrix ===")
print(corr.to_string())

# --- Heatmap ---
fig, ax = plt.subplots(figsize=(8, 6.5))
im = ax.imshow(corr.values, cmap="RdBu_r", vmin=-1, vmax=1)
ax.set_xticks(range(len(corr))); ax.set_yticks(range(len(corr)))
ax.set_xticklabels(corr.columns, rotation=45, ha="right", fontsize=8)
ax.set_yticklabels(corr.index, fontsize=8)
for i in range(len(corr)):
    for j in range(len(corr)):
        ax.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center",
                fontsize=7, color="black")
fig.colorbar(im, ax=ax, shrink=0.8, label="Pearson r")
ax.set_title("E2 — Correlation Among Survey Constructs")
fig.tight_layout()
fig.savefig(BASE / "figures" / "e2_correlation_heatmap.png", dpi=150)
plt.close(fig)

# --- OLS regression (manual, with t-tests) ---
def ols(y, X_cols, data):
    X = np.column_stack([np.ones(len(data))] + [data[c].values for c in X_cols])
    y = y.values
    beta, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    n, p = X.shape
    dof = n - p
    mse = (resid @ resid) / dof
    cov = mse * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    tvals = beta / se
    pvals = 2 * (1 - stats.t.cdf(np.abs(tvals), dof))
    ss_tot = ((y - y.mean()) ** 2).sum()
    ss_res = (resid ** 2).sum()
    r2 = 1 - ss_res / ss_tot
    adj_r2 = 1 - (1 - r2) * (n - 1) / dof
    names = ["(Intercept)"] + X_cols
    out = []
    for nm, b, s, t, pv in zip(names, beta, se, tvals, pvals):
        out.append({"Predictor": nm, "Beta": round(b, 3),
                    "SE": round(s, 3), "t": round(t, 2),
                    "p": round(pv, 4)})
    return out, round(r2, 3), round(adj_r2, 3)

models = {
    "Trust ~ SQ+PE+PS+EM+PR": ("Trust",
        ["Service Quality", "Personalization", "Problem Solving",
         "Perceived Empathy", "Privacy Risk"]),
    "Satisfaction ~ SQ+PE+PS+EM+PR": ("Satisfaction",
        ["Service Quality", "Personalization", "Problem Solving",
         "Perceived Empathy", "Privacy Risk"]),
    "Loyalty ~ Trust+Satisfaction": ("Loyalty Intention",
        ["Trust", "Satisfaction"]),
}

reg_rows = []
print("\n=== OLS Regression Results ===")
for label, (dv, ivs) in models.items():
    coefs, r2, adj = ols(scores_df[dv], ivs, scores_df)
    print(f"\n{label}   (R2={r2}, adj.R2={adj})")
    for c in coefs:
        sig = "***" if c["p"] < 0.001 else "**" if c["p"] < 0.01 else "*" if c["p"] < 0.05 else ""
        print(f"  {c['Predictor']:<18} beta={c['Beta']:>6}  t={c['t']:>6}  p={c['p']:<7} {sig}")
        reg_rows.append({"Model": label, **c, "R2": r2, "adj_R2": adj})

pd.DataFrame(reg_rows).to_csv(
    BASE / "tables" / "e2_regression_results.csv", index=False)
print("\nSaved tables + heatmap.")
