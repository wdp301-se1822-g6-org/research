# Experimental Setup

This study evaluates the proposed AI-powered customer service framework through
three complementary experiments. **E1 uses a real LLM** (Google
`gemini-2.5-flash-lite`) on a real knowledge base; **E2 uses a verified public
survey dataset** from Mendeley Data; **E3 uses synthetic customer data** because
real customer records were not available in this academic setting. All steps are
reproducible, with fixed random seeds where data is generated.

| Exp. | Question addressed | Method | Data |
|---|---|---|---|
| **E1** | RQ1, RQ5 — Does an AI-powered (retrieval-augmented) assistant outperform conventional customer-service baselines? | Real-LLM RAG vs. rule-based and TF-IDF baselines on 50 labelled scenarios | 12-entry KB + 50 annotated scenarios (real `gemini-2.5-flash-lite`) |
| **E2** | RQ1–RQ3 — Which chatbot service factors are associated with trust, satisfaction and loyalty? | Secondary survey analysis; reliability + correlation + OLS regression | Verified public survey from Mendeley Data: 737 raw banking-chatbot responses |
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

**Scenarios (n = 50).** Annotated with the gold knowledge-base entry, whether
human escalation is required, and whether personalization is required.
Distribution: 15 FAQ, 13 loyalty/promotion, 11 personalization, 11
escalation/complaint. Stored in `scenarios.json`.

**Metrics.** Accuracy (correct entry retrieved, or correct escalation),
escalation-handling rate, an automated 1–5 usefulness rubric scored against
ground truth, and response time (real wall-clock latency of the live Gemini API
for S1; sub-millisecond for the baselines). Full LLM answers are saved to
`data/e1_raw_answers_llm.csv` for optional human re-rating.

## E2 — Public Survey Dataset Analysis

**Data source.** E2 uses the verified public dataset **Data on Banking Chatbot
Service Quality** from Mendeley Data (Version 4, DOI:
`10.17632/jsvbvgzkf8.4`, CC BY 4.0). The dataset was contributed by Poornima
Purushotham and published on 2 April 2024. The repository description states
that a structured questionnaire was distributed to Indian banking chatbot users
in Bangalore, India. The local copy is stored in
`data/external/banking_chatbot_mendeley/`, including the raw CSV, questionnaire,
codebook, and IRB clearance file.

**Instrument.** The dataset measures banking chatbot service-quality dimensions
and loyalty outcomes using five-point Likert items. Constructs used in this
study are Semantic Understanding, Human-AI Collaboration, Human-Like
Interaction, Continuous Improvement, Personalization, Cultural Adaptation,
Efficiency, Customer Value, Satisfaction, Trust, and Customer Loyalty.

**Preprocessing.** The original dataset codes missing or incomplete responses as
`0`, and its Likert scale is ordered as 1 = Strongly Agree and 5 = Strongly
disagree. The analysis converts `0` to missing values and reverse-codes Likert
items as `6 - value`, so higher scores consistently represent more positive
perceptions.

**Analysis.** Cronbach's α (reliability threshold 0.70), descriptive statistics,
Pearson correlation matrix, and three standardized OLS regressions:
Trust ~ chatbot service factors; Satisfaction ~ chatbot service factors +
Customer Value; and Customer Loyalty ~ Trust + Satisfaction + Customer Value.
Significance is reported at p < 0.05 / 0.01 / 0.001.

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
python scripts/run_all.py                 # E2 external survey + E3 + simulated E1 reference
# E1 with the real LLM (needs a Gemini key; supports key rotation, resumable cache):
LLM_PROVIDER=gemini LLM_MODEL=gemini-2.5-flash-lite \
  GEMINI_API_KEYS="key1 key2 ..." python scripts/e1_chatbot_eval_llm.py
```

Seeds: E3 = 42. E2 uses a fixed public dataset and does not require random data
generation. E1 LLM run is non-deterministic (temperature 0.2) but cached per
scenario in `data/e1_s1_cache_llm.json` for reproducibility.
Environment: Python 3.13, scikit-learn 1.7, xgboost 3.3, pandas 2.2, numpy 2.2,
scipy 1.15, matplotlib 3.10, google-generativeai 0.8. Model: `gemini-2.5-flash-lite`.
