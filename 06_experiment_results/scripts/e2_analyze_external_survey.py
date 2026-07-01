"""
E2 external survey analysis using a verified public dataset.

Source dataset:
  Purushotham, P. (2024). Data on Banking Chatbot Service Quality.
  Mendeley Data, V4. DOI: 10.17632/jsvbvgzkf8.4

The raw data uses 0 for missing/incomplete answers and a 1..5 Likert scale where
1 = Strongly Agree and 5 = Strongly disagree. This script converts 0 to missing
and reverse-codes Likert answers so higher scores mean more positive evaluation.

Outputs:
  data/e2_external_construct_scores.csv
  tables/e2_external_reliability_descriptives.csv
  tables/e2_external_correlation_matrix.csv
  tables/e2_external_regression_results.csv
  figures/e2_external_correlation_heatmap.png
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data" / "external" / "banking_chatbot_mendeley" / "banking_chatbot_raw.csv"

CONSTRUCTS = {
    "Semantic Understanding": ["Sem_1", "Sem_2", "Sem_3", "Sem_4", "Sem_5"],
    "Human-AI Collaboration": ["Hc_1", "Hc_2", "Hc_3", "Hc_4", "Hc_5", "Hc_6"],
    "Human-Like Interaction": ["Hl_1", "Hl_2", "Hl_3", "Hl_4"],
    "Continuous Improvement": ["CI_1", "CI_2", "CI_3", "CI_4"],
    "Personalization": ["PERSN_1", "PERSN_2", "PERSN_3", "PERSN_4"],
    "Cultural Adaptation": ["Ca_1", "Ca_2", "Ca_3", "Ca_4"],
    "Efficiency": ["Ey_1", "Ey_2", "Ey_3", "Ey_ 4"],
    "Customer Value": ["Cv_1", "Cv_2", "Cv_3", "CV_4"],
    "Satisfaction": ["CS_1", "CS_2", "CS_3", "CS_4", "CS_5"],
    "Trust": ["CT_1", "CT_2", "CT_3", "CT_4", "CT_5"],
    "Customer Loyalty": ["CL_1", "CL_2", "CL_3", "CL_4", "CL_5"],
}

SERVICE_FACTORS = [
    "Semantic Understanding",
    "Human-AI Collaboration",
    "Human-Like Interaction",
    "Continuous Improvement",
    "Personalization",
    "Cultural Adaptation",
    "Efficiency",
]


def cronbach_alpha(items_df):
    items_df = items_df.dropna()
    if len(items_df) < 2:
        return np.nan
    k = items_df.shape[1]
    item_var = items_df.var(axis=0, ddof=1).sum()
    total_var = items_df.sum(axis=1).var(ddof=1)
    if total_var == 0:
        return np.nan
    return (k / (k - 1)) * (1 - item_var / total_var)


def zscore(frame):
    return (frame - frame.mean()) / frame.std(ddof=1)


def ols_standardized(data, y_col, x_cols, label):
    model_data = data[[y_col] + x_cols].dropna()
    zdata = zscore(model_data)
    X = np.column_stack([np.ones(len(zdata))] + [zdata[c].values for c in x_cols])
    y = zdata[y_col].values

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

    rows = []
    for name, b, s, t, pv in zip(["(Intercept)"] + x_cols, beta, se, tvals, pvals):
        rows.append(
            {
                "Model": label,
                "N": n,
                "Predictor": name,
                "Beta": round(float(b), 3),
                "SE": round(float(s), 3),
                "t": round(float(t), 2),
                "p": round(float(pv), 4),
                "R2": round(float(r2), 3),
                "adj_R2": round(float(adj_r2), 3),
            }
        )
    return rows


def main():
    df = pd.read_csv(RAW)
    all_items = [col for items in CONSTRUCTS.values() for col in items]
    likert = df[all_items].replace(0, np.nan)
    likert = 6 - likert

    rel_rows = []
    scores = {}
    for construct, items in CONSTRUCTS.items():
        sub = likert[items]
        score = sub.mean(axis=1, skipna=True)
        scores[construct] = score
        rel_rows.append(
            {
                "Construct": construct,
                "Items": len(items),
                "Valid_N": int(sub.dropna().shape[0]),
                "Score_N": int(score.notna().sum()),
                "Mean": round(float(score.mean()), 3),
                "SD": round(float(score.std(ddof=1)), 3),
                "Cronbach_alpha": round(float(cronbach_alpha(sub)), 3),
            }
        )

    scores_df = pd.DataFrame(scores)
    scores_df.insert(0, "record_id", df["record_id"])
    scores_df.to_csv(BASE / "data" / "e2_external_construct_scores.csv", index=False)

    rel = pd.DataFrame(rel_rows)
    rel.to_csv(BASE / "tables" / "e2_external_reliability_descriptives.csv", index=False)
    print("=== E2 External Survey: Reliability & Descriptives ===")
    print(rel.to_string(index=False))

    corr = scores_df.drop(columns=["record_id"]).corr(method="pearson").round(3)
    corr.to_csv(BASE / "tables" / "e2_external_correlation_matrix.csv")
    print("\n=== E2 External Survey: Pearson Correlation Matrix ===")
    print(corr.to_string())

    regression_rows = []
    regression_rows += ols_standardized(
        scores_df,
        "Trust",
        SERVICE_FACTORS,
        "Trust ~ chatbot service factors",
    )
    regression_rows += ols_standardized(
        scores_df,
        "Satisfaction",
        SERVICE_FACTORS + ["Customer Value"],
        "Satisfaction ~ chatbot service factors + Customer Value",
    )
    regression_rows += ols_standardized(
        scores_df,
        "Customer Loyalty",
        ["Trust", "Satisfaction", "Customer Value"],
        "Customer Loyalty ~ Trust + Satisfaction + Customer Value",
    )
    reg = pd.DataFrame(regression_rows)
    reg.to_csv(BASE / "tables" / "e2_external_regression_results.csv", index=False)
    print("\n=== E2 External Survey: OLS Regression Results ===")
    for model, group in reg.groupby("Model", sort=False):
        first = group.iloc[0]
        print(f"\n{model} (N={int(first['N'])}, R2={first['R2']}, adj.R2={first['adj_R2']})")
        for _, row in group.iterrows():
            sig = "***" if row["p"] < 0.001 else "**" if row["p"] < 0.01 else "*" if row["p"] < 0.05 else ""
            print(f"  {row['Predictor']:<32} beta={row['Beta']:>6}  t={row['t']:>6}  p={row['p']:<7} {sig}")

    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(corr.values, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr)))
    ax.set_yticks(range(len(corr)))
    ax.set_xticklabels(corr.columns, rotation=45, ha="right", fontsize=8)
    ax.set_yticklabels(corr.index, fontsize=8)
    for i in range(len(corr)):
        for j in range(len(corr)):
            ax.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center", fontsize=7)
    fig.colorbar(im, ax=ax, shrink=0.8, label="Pearson r")
    ax.set_title("E2 External Survey - Banking Chatbot Constructs")
    fig.tight_layout()
    fig.savefig(BASE / "figures" / "e2_external_correlation_heatmap.png", dpi=150)
    plt.close(fig)
    print("\nSaved E2 external survey tables, construct scores, and heatmap.")


if __name__ == "__main__":
    main()
