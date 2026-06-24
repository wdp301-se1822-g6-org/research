"""
E3 - Train and evaluate loyalty-retention prediction models.

Compares a majority-class baseline against Logistic Regression, Random Forest,
and XGBoost. Uses an 80/20 stratified split, 5-fold CV with GridSearchCV for
hyper-parameter tuning, and reports Accuracy / Precision / Recall / F1 / ROC-AUC
on the held-out test set. Also produces an ROC-curve figure and a feature
importance figure.

Outputs:
  tables/e3_model_comparison.csv
  figures/e3_roc_curve.png
  figures/e3_feature_importance.png
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, roc_curve)
from xgboost import XGBClassifier

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE / "data" / "customers.csv")

FEATURES = ["num_interactions", "purchase_freq_per_month", "loyalty_points",
            "tier_rank", "chatbot_usage_freq", "avg_satisfaction_score",
            "avg_trust_score", "complaint_count_3m", "days_since_last_active"]
X = df[FEATURES].values
y = df["will_retain_next_6m"].values

X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42)

results = []
roc_data = {}
rf_importances = None

def evaluate(name, y_true, y_pred, y_proba):
    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred, zero_division=0),
        "Recall": recall_score(y_true, y_pred, zero_division=0),
        "F1": f1_score(y_true, y_pred, zero_division=0),
        "ROC_AUC": roc_auc_score(y_true, y_proba) if y_proba is not None else np.nan,
    })
    if y_proba is not None:
        fpr, tpr, _ = roc_curve(y_true, y_proba)
        roc_data[name] = (fpr, tpr, roc_auc_score(y_true, y_proba))

# --- Baseline: majority class ---
dummy = DummyClassifier(strategy="most_frequent").fit(X_tr, y_tr)
evaluate("Baseline (majority)", y_te, dummy.predict(X_te),
         dummy.predict_proba(X_te)[:, 1])

# --- Logistic Regression ---
lr = GridSearchCV(
    Pipeline([("sc", StandardScaler()),
              ("clf", LogisticRegression(max_iter=1000))]),
    {"clf__C": [0.1, 1, 10]}, cv=5, scoring="f1").fit(X_tr, y_tr)
evaluate("Logistic Regression", y_te, lr.predict(X_te),
         lr.predict_proba(X_te)[:, 1])

# --- Random Forest ---
rf = GridSearchCV(
    RandomForestClassifier(random_state=42),
    {"n_estimators": [50, 100, 200], "max_depth": [None, 6, 10]},
    cv=5, scoring="f1").fit(X_tr, y_tr)
evaluate("Random Forest", y_te, rf.predict(X_te),
         rf.predict_proba(X_te)[:, 1])
rf_importances = rf.best_estimator_.feature_importances_

# --- XGBoost ---
xgb = GridSearchCV(
    XGBClassifier(eval_metric="logloss", random_state=42),
    {"max_depth": [3, 5, 7], "n_estimators": [100, 200]},
    cv=5, scoring="f1").fit(X_tr, y_tr)
evaluate("XGBoost", y_te, xgb.predict(X_te),
         xgb.predict_proba(X_te)[:, 1])

res = pd.DataFrame(results).round(4)
(BASE / "tables").mkdir(exist_ok=True)
res.to_csv(BASE / "tables" / "e3_model_comparison.csv", index=False)
print(res.to_string(index=False))
print("\nBest params:")
print("  LogReg:", lr.best_params_)
print("  RF    :", rf.best_params_)
print("  XGB   :", xgb.best_params_)

# --- ROC curve figure ---
plt.figure(figsize=(6, 5))
for name, (fpr, tpr, auc) in roc_data.items():
    if name.startswith("Baseline"):
        continue
    plt.plot(fpr, tpr, label=f"{name} (AUC={auc:.3f})")
plt.plot([0, 1], [0, 1], "k--", alpha=0.4, label="Random")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("E3 — ROC Curves: Loyalty-Retention Prediction")
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig(BASE / "figures" / "e3_roc_curve.png", dpi=150)
plt.close()

# --- Feature importance figure (Random Forest) ---
order = np.argsort(rf_importances)
plt.figure(figsize=(7, 5))
plt.barh(np.array(FEATURES)[order], rf_importances[order], color="#4C78A8")
plt.xlabel("Importance (Random Forest)")
plt.title("E3 — Feature Importance for Retention Prediction")
plt.tight_layout()
plt.savefig(BASE / "figures" / "e3_feature_importance.png", dpi=150)
plt.close()
print("\nFigures saved: e3_roc_curve.png, e3_feature_importance.png")
