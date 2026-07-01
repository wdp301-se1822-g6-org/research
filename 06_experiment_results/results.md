# Experimental Results

All results below are produced by the experiment scripts and are fully
reproducible. E1 uses a real LLM with cached outputs, E2 uses a verified public
survey dataset from Mendeley Data, and E3 uses synthetic customer data with a
fixed random seed. Numbers are reported to three decimals.

---

## E1 — Chatbot Prototype vs. Baselines (50 scenarios)

S1 (the proposed assistant) is implemented with a **real LLM** — Google
`gemini-2.5-flash-lite` via the Gemini API — using TF-IDF retrieval of the
top-3 knowledge-base entries as grounding context (true retrieval-augmented
generation). B1 and B2 remain the deterministic rule-based and TF-IDF baselines.
The benchmark has 50 annotated scenarios (15 FAQ, 13 loyalty, 11
personalization, 11 escalation). Response times are real wall-clock
measurements of the live API.

**Table 1. Overall system comparison.**

| System | Avg. Response Time (s) | Avg. Usefulness (1–5) | Accuracy (%) | Escalation Handling (%) |
|---|---:|---:|---:|---:|
| **S1 (Proposed RAG, real LLM)** | 11.46 | **3.98** | **88.0** | **98.0** |
| B1 (Rule-based) | <0.001 | 3.04 | 68.0 | 78.0 |
| B2 (TF-IDF) | <0.001 | 3.12 | 64.0 | 78.0 |

**Table 2. Accuracy (%) by scenario category.**

| System | FAQ | Loyalty | Personalization | Escalation |
|---|---:|---:|---:|---:|
| **S1 (Proposed RAG, real LLM)** | 93.3 | **92.3** | 63.6 | **100.0** |
| B1 (Rule-based) | 93.3 | 76.9 | 45.5 | 45.5 |
| B2 (TF-IDF) | 93.3 | 76.9 | **72.7** | 0.0 |

**Findings.**

- Over 50 scenarios the proposed assistant (S1) reached **88.0% overall accuracy
  and a 3.98/5 usefulness score**, versus 64–68% accuracy and ≤3.12 usefulness
  for both baselines — a relative usefulness gain of **28–31%**.
- S1's largest, most consistent advantage is **escalation**: it detected all 11
  complaint/security cases (100% vs. 45.5%/0%), politely routing them to a human
  while the baselines answered them inappropriately. It also led on **loyalty**
  explanations (92.3% vs. 76.9%).
- The real LLM performed genuine reasoning the baselines cannot: for *"I have
  1,200 points, how many more to reach Gold?"* it answered *"Gold needs 1,500
  points, so you are 300 short,"* computing the gap from the grounded rule.
- The trade-off is **latency**: S1 averages 11.46 s of real API time (network +
  inference), whereas the baselines respond in under 1 ms — the expected
  efficiency-versus-quality paradox of generative AI service (Ferraro et al.,
  2024).
- The honest failure modes: S1 lost on personalization (63.6%) when the customer
  context was not in the prompt — it correctly asked a clarifying question
  instead of inventing an answer — and it **over-escalated one FAQ** (an account
  query it routed to a human), the single reason escalation handling is 98%
  rather than 100%. Over-escalation is a safer error than wrong automation.

*Figure: `figures/e1_system_comparison.png` — usefulness and accuracy bars.
Per-scenario data: `data/e1_per_scenario_llm.csv`; full LLM answers:
`data/e1_raw_answers_llm.csv`.*

---

## E2 — Public Survey Dataset (Mendeley Data, banking chatbot users)

E2 now uses a **verified public survey dataset** rather than simulated
respondents: *Data on Banking Chatbot Service Quality*, Mendeley Data V4,
DOI `10.17632/jsvbvgzkf8.4`, CC BY 4.0. The raw dataset contains 737 banking
chatbot survey responses. The original file codes missing/incomplete answers as
`0` and uses 1 = Strongly Agree through 5 = Strongly disagree, so the analysis
converts `0` to missing values and reverse-codes Likert items as `6 - value`.

**Table 3. Reliability and descriptive statistics.**

| Construct | Score N | Mean | SD | Cronbach's α |
|---|---:|---:|---:|---:|
| Semantic Understanding | 648 | 3.16 | 0.72 | 0.895 |
| Human-AI Collaboration | 647 | 3.17 | 0.73 | 0.903 |
| Human-Like Interaction | 647 | 3.07 | 0.78 | 0.880 |
| Continuous Improvement | 651 | 3.18 | 0.69 | 0.749 |
| Personalization | 651 | 3.07 | 0.72 | 0.755 |
| Cultural Adaptation | 651 | 3.11 | 0.72 | 0.771 |
| Efficiency | 651 | 3.14 | 0.79 | 0.881 |
| Customer Value | 644 | 3.12 | 0.73 | 0.761 |
| Satisfaction | 724 | 3.15 | 0.69 | 0.827 |
| Trust | 724 | 3.14 | 0.70 | 0.785 |
| Customer Loyalty | 724 | 3.13 | 0.72 | 0.802 |

All constructs exceed the 0.70 reliability threshold (α = 0.749–0.903), so the
measurement scales are internally consistent after reverse-coding.

**Table 4. Selected Pearson correlations.**

| Pair | r |
|---|---:|
| Trust ↔ Customer Loyalty | 0.736 |
| Satisfaction ↔ Customer Loyalty | 0.718 |
| Trust ↔ Satisfaction | 0.660 |
| Customer Value ↔ Trust | 0.317 |
| Customer Value ↔ Customer Loyalty | 0.305 |
| Personalization ↔ Customer Loyalty | 0.225 |

Trust and Satisfaction show the strongest associations with Customer Loyalty,
which is consistent with the proposed loyalty pathway.

**Table 5. OLS regression results** (standardized predictors; *** p<0.001,
** p<0.01, * p<0.05).

*Model 1 — Trust ~ chatbot service factors (N = 645, R² = 0.095, adj. R² = 0.085)*

| Predictor | β | t | p | |
|---|---:|---:|---:|---|
| Semantic Understanding | 0.170 | 3.37 | 0.0008 | *** |
| Human-AI Collaboration | −0.019 | −0.33 | 0.741 | ns |
| Human-Like Interaction | −0.069 | −1.25 | 0.213 | ns |
| Continuous Improvement | 0.029 | 0.53 | 0.599 | ns |
| Personalization | 0.003 | 0.05 | 0.962 | ns |
| Cultural Adaptation | 0.175 | 3.22 | 0.0013 | ** |
| Efficiency | 0.062 | 1.30 | 0.194 | ns |

*Model 2 — Satisfaction ~ chatbot service factors + Customer Value (N = 640, R² = 0.107, adj. R² = 0.096)*

| Predictor | β | t | p | |
|---|---:|---:|---:|---|
| Semantic Understanding | 0.180 | 3.51 | 0.0005 | *** |
| Human-AI Collaboration | −0.045 | −0.80 | 0.421 | ns |
| Human-Like Interaction | −0.028 | −0.51 | 0.614 | ns |
| Continuous Improvement | −0.063 | −1.14 | 0.253 | ns |
| Personalization | 0.055 | 1.01 | 0.314 | ns |
| Cultural Adaptation | 0.140 | 2.54 | 0.011 | * |
| Efficiency | −0.014 | −0.30 | 0.764 | ns |
| Customer Value | 0.139 | 2.73 | 0.0065 | ** |

*Model 3 — Customer Loyalty ~ Trust + Satisfaction + Customer Value (N = 644, R² = 0.649, adj. R² = 0.647)*

| Predictor | β | t | p | |
|---|---:|---:|---:|---|
| Trust | 0.440 | 13.89 | <0.001 | *** |
| Satisfaction | 0.424 | 13.59 | <0.001 | *** |
| Customer Value | 0.053 | 2.15 | 0.032 | * |

**Findings.**

- **Semantic understanding and cultural adaptation significantly increase Trust**
  in the verified banking-chatbot survey data, supporting the importance of
  accurate understanding and context-fit in AI service quality.
- **Semantic understanding, cultural adaptation, and customer value significantly
  increase Satisfaction**, while the other service dimensions are not significant
  after controlling for overlapping service-quality factors.
- **Trust and Satisfaction are the dominant predictors of Customer Loyalty**
  (Model 3, R² = 0.649), supporting RQ3 with a real public survey dataset rather
  than simulated responses.

*Figure: `figures/e2_external_correlation_heatmap.png`.*

---

## E3 — Loyalty-Retention Prediction (n = 1,000 simulated customers)

**Table 6. Model comparison on the held-out test set (20%).**

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Baseline (majority) | 0.670 | 0.670 | 1.000 | 0.802 | 0.500 |
| **Logistic Regression** | **0.770** | **0.779** | 0.918 | **0.843** | **0.806** |
| Random Forest | 0.755 | 0.767 | 0.910 | 0.833 | 0.799 |
| XGBoost | 0.720 | 0.753 | 0.866 | 0.806 | 0.761 |

Best hyper-parameters: LogReg C = 0.1; RF n_estimators = 100, max_depth = None;
XGBoost max_depth = 7, n_estimators = 200.

**Findings.**

- All learned models beat the majority-class baseline on the discriminative
  metrics. The baseline's F1 (0.802) looks high only because it labels everyone
  "retain" (recall = 1.0), but its **ROC-AUC of 0.500 shows zero discriminative
  power**.
- **Logistic Regression performs best** (Accuracy 0.770, F1 0.843, AUC 0.806),
  marginally ahead of Random Forest and XGBoost. This is consistent with the
  underlying data-generating process being approximately logistic, and shows a
  simple, interpretable model is sufficient for this task.
- Random-Forest feature importance ranks **average satisfaction, average trust,
  recency (days since last active), and purchase frequency** as the strongest
  retention predictors — the same constructs that the E2 survey links to
  loyalty, giving cross-experiment convergence.

*Figures: `figures/e3_roc_curve.png`, `figures/e3_feature_importance.png`.*

---

## Cross-Experiment Synthesis

The three experiments triangulate the central claim of the paper:

1. **E1** shows a real-LLM AI-powered assistant delivers materially better
   service quality on the hard, loyalty-relevant interactions (escalation and
   loyalty explanations) than conventional baselines.
2. **E2** shows, using a verified public banking-chatbot survey dataset, that
   semantic understanding and cultural adaptation are associated with **trust**
   and **satisfaction**, and that trust and satisfaction strongly drive
   **customer loyalty**.
3. **E3** shows that the **behavioural signals of trust, satisfaction,
   engagement and recency** are predictive of retention, enabling a loyalty
   prediction module to flag at-risk customers.

Together they support the proposed framework: AI service quality → trust /
satisfaction → loyalty outcomes, with an operational prediction layer for
proactive retention.

## Threats to Validity

- **E2 secondary-data scope.** E2 now uses a verified public dataset rather than
  simulated respondents, but it is secondary data from banking chatbot users in
  India. The findings may not generalize to every smart service ecosystem, and
  the dataset does not directly measure privacy risk.
- **Synthetic data in E3.** E3 uses synthetic customers, so it demonstrates the
  prediction pipeline and expected relationships but must be confirmed on real
  customer records.
- **E1 scoring.** E1 uses a **real LLM** on a real knowledge base, but its
  usefulness is scored with an automated rubric rather than human raters; the
  full LLM answers are saved (`e1_raw_answers_llm.csv`) for optional human
  re-rating with inter-rater reliability.
- **E1 scope.** The knowledge base and 50 scenarios are a controlled benchmark;
  a larger, real customer-query distribution may yield different accuracy, and
  LLM latency depends on the chosen model and API conditions.

These are revisited in the Discussion and Future Work sections.
