# Experimental Results

All results below are produced by `scripts/run_all.py` on simulated data with
fixed seeds and are fully reproducible. Numbers are reported to three decimals.

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

## E2 — User Survey (n = 52, simulated pilot)

**Table 3. Reliability and descriptive statistics.**

| Construct | Mean | SD | Cronbach's α |
|---|---:|---:|---:|
| AI Service Quality | 3.76 | 0.72 | 0.859 |
| Personalization | 3.33 | 0.79 | 0.877 |
| Problem Solving | 3.68 | 0.80 | 0.898 |
| Perceived Empathy | 3.29 | 0.89 | 0.912 |
| Privacy Risk | 3.08 | 0.78 | 0.886 |
| Trust | 3.62 | 0.63 | 0.730 |
| Satisfaction | 3.67 | 0.71 | 0.820 |
| Loyalty Intention | 3.47 | 0.69 | 0.849 |

All constructs exceed the 0.70 reliability threshold (α = 0.730–0.912), so the
measurement scales are internally consistent.

**Table 4. Selected Pearson correlations.**

| Pair | r |
|---|---:|
| Trust ↔ Loyalty Intention | 0.782 |
| Problem Solving ↔ Trust | 0.551 |
| Personalization ↔ Trust | 0.533 |
| Satisfaction ↔ Loyalty Intention | 0.473 |
| Privacy Risk ↔ Satisfaction | −0.388 |
| Privacy Risk ↔ Trust | −0.269 |

Trust shows the strongest association with loyalty intention (r = 0.782), and
privacy risk is consistently negatively correlated with trust and satisfaction.

**Table 5. OLS regression results** (standardized-scale predictors; *** p<0.001,
** p<0.01, * p<0.05).

*Model 1 — Trust ~ service factors (R² = 0.636, adj. R² = 0.596)*

| Predictor | β | t | p | |
|---|---:|---:|---:|---|
| Service Quality | 0.202 | 2.45 | 0.018 | * |
| Personalization | 0.291 | 3.84 | 0.0004 | *** |
| Problem Solving | 0.291 | 3.91 | 0.0003 | *** |
| Perceived Empathy | 0.198 | 2.97 | 0.005 | ** |
| Privacy Risk | −0.102 | −1.37 | 0.178 | ns |

*Model 2 — Satisfaction ~ service factors (R² = 0.509, adj. R² = 0.456)*

| Predictor | β | t | p | |
|---|---:|---:|---:|---|
| Service Quality | 0.224 | 2.10 | 0.041 | * |
| Personalization | 0.229 | 2.34 | 0.024 | * |
| Problem Solving | 0.344 | 3.56 | 0.0009 | *** |
| Perceived Empathy | −0.001 | −0.01 | 0.994 | ns |
| Privacy Risk | −0.275 | −2.86 | 0.006 | ** |

*Model 3 — Loyalty Intention ~ Trust + Satisfaction (R² = 0.647, adj. R² = 0.633)*

| Predictor | β | t | p | |
|---|---:|---:|---:|---|
| Trust | 0.766 | 7.67 | <0.001 | *** |
| Satisfaction | 0.198 | 2.21 | 0.032 | * |

**Findings.**

- **Service quality, personalization, problem-solving and perceived empathy all
  significantly increase Trust** (Model 1, R² = 0.64), supporting RQ1/RQ2.
- **Problem-solving most strongly drives Satisfaction** (β = 0.344, p < 0.001),
  and **privacy risk significantly reduces Satisfaction** (β = −0.275,
  p < 0.01), confirming the risk pathway in RQ2.
- **Trust is the dominant predictor of Loyalty Intention** (β = 0.766,
  p < 0.001), with satisfaction adding a smaller significant contribution
  (Model 3, R² = 0.65). This supports RQ3: trust and satisfaction mediate the
  link from AI service factors to loyalty.

*Figure: `figures/e2_correlation_heatmap.png`.*

---

## E3 — Loyalty-Retention Prediction (n = 1,000 simulated customers)

**Table 6. Model comparison on the held-out test set (20%).**

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Baseline (majority) | 0.670 | 0.670 | 1.000 | 0.802 | 0.500 |
| **Logistic Regression** | **0.770** | **0.779** | 0.918 | **0.843** | **0.806** |
| Random Forest | 0.755 | 0.767 | 0.910 | 0.833 | 0.799 |
| XGBoost | 0.745 | 0.771 | 0.881 | 0.822 | 0.764 |

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
2. **E2** shows that those same service factors — quality, personalization,
   problem-solving, empathy — significantly raise **trust and satisfaction**,
   which in turn drive **loyalty intention**, while privacy risk erodes
   satisfaction.
3. **E3** shows that the **behavioural signals of trust, satisfaction,
   engagement and recency** are predictive of retention, enabling a loyalty
   prediction module to flag at-risk customers.

Together they support the proposed framework: AI service quality → trust /
satisfaction → loyalty outcomes, with an operational prediction layer for
proactive retention.

## Threats to Validity

- **Simulated data in E2 and E3.** E2 and E3 use synthetic respondents/customers,
  so they demonstrate the methodology and expected relationships but must be
  confirmed on real data. E1 instead uses a **real LLM** on a real knowledge
  base, but its usefulness is scored with an automated rubric rather than human
  raters; the full LLM answers are saved (`e1_raw_answers_llm.csv`) for optional
  human re-rating with inter-rater reliability.
- **Construct relationships in E2 are partly encoded in the data-generating
  model**; the experiment validates the analysis pipeline and effect direction,
  not external generalizability.
- **E1 scope.** The knowledge base and 50 scenarios are a controlled benchmark;
  a larger, real customer-query distribution may yield different accuracy, and
  LLM latency depends on the chosen model and API conditions.

These are revisited in the Discussion and Future Work sections.
