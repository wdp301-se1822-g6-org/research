# Experimental Setup

This study evaluates the proposed AI-powered customer service framework through
three complementary experiments. **E1 uses a real LLM** (Google
`gemini-2.5-flash-lite`) on a real knowledge base; **E2 and E3 use
simulated / synthetic data**, clearly labelled as such, because real users and
customer records were not available in this academic setting. All steps are
reproducible with fixed random seeds.

| Exp. | Question addressed | Method | Data |
|---|---|---|---|
| **E1** | RQ1, RQ5 — Does an AI-powered (retrieval-augmented) assistant outperform conventional customer-service baselines? | Real-LLM RAG vs. rule-based and TF-IDF baselines on 30 labelled scenarios | 12-entry KB + 30 annotated scenarios (real `gemini-2.5-flash-lite`) |
| **E2** | RQ1–RQ3 — Which service factors drive trust, satisfaction and loyalty intention? | 24-item, 8-construct Likert questionnaire; reliability + correlation + OLS regression | 52 simulated respondents |
| **E3** | RQ4 — Can customer behaviour predict loyalty retention / tier progression? | Majority baseline vs. Logistic Regression, Random Forest, XGBoost | 1,000 simulated customers |

## E1 — Chatbot Prototype Evaluation

**Systems compared.**

- **S1 (Proposed, retrieval-augmented assistant):** a **real LLM**
  (`gemini-2.5-flash-lite`) grounded on the knowledge base. For each query the
  top-3 KB entries are retrieved with TF-IDF and inserted into a Vietnamese
  prompt instructing the model to answer only from the KB, escalate
  complaint/security cases to a human, and personalize when the query references
  the customer's own context. The model returns structured JSON
  (answer, KB id used, escalate, personalized).
- **B1 (Rule-based baseline):** brittle keyword/intent matcher returning fixed
  answers — representative of a conventional FAQ bot.
- **B2 (Keyword-search baseline):** TF-IDF cosine retrieval, top-1 answer, with
  no escalation or personalization.

**Knowledge base.** 12 canonical entries covering opening hours, cancellation
policy, payment, booking, loyalty points, membership tiers, vouchers, account
recovery, refund timing, contact, and data privacy (Vietnamese content for a
smart booking/service platform with a 4-tier loyalty program).

**Scenarios (n = 30).** Annotated with the gold knowledge-base entry, whether
human escalation is required, and whether personalization is required.
Distribution: 10 FAQ, 8 loyalty/promotion, 6 personalization, 6
escalation/complaint. Stored in `scenarios.json`.

**Metrics.** Accuracy (correct entry retrieved, or correct escalation),
escalation-handling rate, an automated 1–5 usefulness rubric scored against
ground truth, and response time (real wall-clock latency of the live Gemini API
for S1; sub-millisecond for the baselines). Full LLM answers are saved to
`data/e1_raw_answers_llm.csv` for optional human re-rating.

## E2 — User Survey (simulated pilot)

**Instrument.** 8 constructs × 3 items, 5-point Likert: AI Service Quality,
Personalization, Problem Solving, Perceived Empathy, Privacy Risk, Trust,
Satisfaction, Loyalty Intention. Items follow the survey constructs defined in
`05_methodology/methodology.md`.

**Respondents.** 52 simulated respondents generated from a latent structural
model that encodes the proposed research model
(Trust/Satisfaction ← service factors − privacy risk; Loyalty ← Trust +
Satisfaction), plus demographic fields (age, gender, prior chatbot use).

**Analysis.** Cronbach's α (reliability, threshold 0.70), descriptive
statistics, Pearson correlation matrix, and three OLS regressions matching the
hypothesized paths. Significance reported at p < 0.05 / 0.01 / 0.001.

## E3 — Loyalty-Retention Prediction

**Dataset.** 1,000 simulated customers with nine behavioural/engagement
features (interactions, purchase frequency, loyalty points, tier rank, chatbot
usage, satisfaction, trust, complaints, recency). The binary target
`will_retain_next_6m` is drawn from a known logistic data-generating process
with Gaussian noise, yielding ~67% retention (a non-trivial majority baseline).

**Protocol.** 80/20 stratified train/test split; 5-fold cross-validated
`GridSearchCV` hyper-parameter tuning on the training set; evaluation on the
held-out test set.

**Models.** Majority-class baseline, Logistic Regression (C ∈ {0.1, 1, 10}),
Random Forest (n_estimators ∈ {50,100,200}, max_depth ∈ {None,6,10}), XGBoost
(max_depth ∈ {3,5,7}, n_estimators ∈ {100,200}).

**Metrics.** Accuracy, Precision, Recall, F1-score, ROC-AUC, plus Random-Forest
feature importance.

## Reproducibility

```bash
cd 06_experiment_results
python scripts/run_all.py                 # E2 + E3 (and the simulated E1 reference)
# E1 with the real LLM (needs a Gemini key; supports key rotation, resumable cache):
LLM_PROVIDER=gemini LLM_MODEL=gemini-2.5-flash-lite \
  GEMINI_API_KEYS="key1 key2 ..." python scripts/e1_chatbot_eval_llm.py
```

Seeds: E2 = 7, E3 = 42. E1 LLM run is non-deterministic (temperature 0.2) but
cached per scenario in `data/e1_s1_cache_llm.json` for reproducibility.
Environment: Python 3.13, scikit-learn 1.7, xgboost 3.3, pandas 2.2, numpy 2.2,
scipy 1.15, matplotlib 3.10, google-generativeai 0.8. Model: `gemini-2.5-flash-lite`.
