# AI-Powered Customer Service for Improving Customer Loyalty in Smart Service Ecosystems

## Obsidian Links

- Map: [[research_map|Research Map]]
- Source topic: [[01_topic_proposal/topic_proposal|Topic Proposal]]
- Related work: [[02_related_work/literature_review_matrix|Literature Review Matrix]]
- Problem and gap: [[03_problem_and_gap/problem_statement|Problem Statement]], [[03_problem_and_gap/research_gap|Research Gap]], [[03_problem_and_gap/research_questions|Research Questions]]
- Proposed system: [[04_proposed_system/system_overview|System Overview]], [[04_proposed_system/system_architecture|System Architecture]], [[04_proposed_system/ai_model_integration|AI Model Integration]], [[04_proposed_system/data_flow|Data Flow]]
- Methodology: [[05_methodology/methodology|Methodology]], [[05_methodology/dataset|Dataset]], [[05_methodology/baseline|Baseline]], [[05_methodology/evaluation_metrics|Evaluation Metrics]]
- Experiments: [[06_experiment_results/experimental_setup|Experimental Setup]], [[06_experiment_results/results|Results]], [[06_experiment_results/experiment_plan|Experiment Plan]]
- Weekly progress: [[weekly_reports/week_04|Week 04]], [[weekly_reports/week_05|Week 05]]

## Group Information

- Class: SE1822
- Group: Group 6
- Leader: Đinh Hoàng Kha (SE193633)
- Members:
  - Nguyễn Quốc Đoàn (SE180466)
  - Trần Hữu Phước (SE180579)
  - Nguyễn Minh Châu (SE180582)
  - Nguyễn Trần Minh Hưng (SE193002)

## Lecturer Information and Response

- Lecturer: Trương Long
- Email: longt5@fe.edu.vn

### Lecturer Response

[Add the lecturer's response or feedback here.]

---

## Abstract

AI-powered customer service has become an important component of smart service ecosystems because customers increasingly expect fast, accurate, personalized, and convenient support. Prior studies show that AI chatbots and generative AI service tools can improve customer experience, satisfaction, trust, continuance intention, and e-brand loyalty, but they also raise risks such as privacy concerns, limited empathy, and over-reliance on automation. However, most prior work examines AI customer service and loyalty programs separately, leaving the link between AI service factors and loyalty outcomes underexplored. This study investigates how AI-powered customer service factors influence customer loyalty in smart service ecosystems by integrating an existing retrieval-augmented chatbot and an optional loyalty-prediction module into a customer service platform, rather than training a new model from scratch. We evaluate the framework through three reproducible experiments: (E1) a prototype chatbot built on a real LLM (Google gemini-2.5-flash-lite), benchmarked against rule-based and keyword-search baselines on 50 annotated scenarios; (E2) a verified public banking-chatbot survey from Mendeley Data (737 raw responses) analyzed with reliability, correlation, and regression; and (E3) a loyalty-retention prediction task comparing four models on 1,000 simulated customers. The proposed assistant achieved 88.0% accuracy and a 3.98/5 usefulness score with 98% correct escalation, clearly outperforming the baselines (64–68% accuracy). The external survey analysis confirmed reliable measurement scales (Cronbach's α = 0.749–0.903) and showed that trust and satisfaction are the dominant predictors of customer loyalty (β = 0.440 and 0.424, p < 0.001, R² = 0.649). The best prediction model (Logistic Regression) reached an F1 of 0.843 and ROC-AUC of 0.806, well above the majority baseline. The contribution is a practical, evaluated AI customer service framework linking AI service quality to trust, satisfaction, and loyalty outcomes, with an operational prediction layer for proactive retention.

**Keywords:** AI-powered customer service, AI chatbot, customer loyalty, customer retention, trust, satisfaction, loyalty tier progression, smart service ecosystem.

---

## 1. Introduction

Digital service platforms have changed the way customers interact with businesses. Customers now expect service providers to offer quick responses, accurate information, personalized recommendations, and convenient support across multiple digital channels. In this context, customer service is no longer only a support function; it has become an important part of customer experience and customer relationship management.

Traditional customer service often depends heavily on human staff, which can create slow response time, inconsistent service quality, limited personalization, and high operating cost. AI-powered customer service, especially chatbot-based support, can help address these limitations by answering customer questions, explaining promotions, recommending suitable services, supporting booking or purchasing decisions, and collecting customer feedback. With the development of large language models and generative AI, customer service chatbots can also provide more natural and context-aware interactions.

Customer loyalty matters because retaining existing customers is usually more cost-effective than acquiring new ones. In smart service ecosystems, loyalty appears through repeated usage, continued engagement, positive word of mouth, reward redemption, and loyalty tier progression. Yet businesses still need to understand which AI-powered service factors actually support these loyalty outcomes.

### 1.1 Problem Statement

In modern smart service ecosystems, customers expect fast, accurate, and personalized support, but traditional customer service is limited by staff availability, inconsistent quality, and long waiting times. AI-powered chatbots can improve service efficiency, but improving efficiency alone is not enough: businesses also need to know whether AI customer service can strengthen loyalty, retention, long-term engagement, and movement across loyalty tiers. Prior studies show that chatbot service quality, personalization, interaction, trust, satisfaction, empathy, and problem-solving ability affect customer experience and continued usage, while privacy risk, lack of empathy, and unreliable responses can reduce trust and satisfaction. The core problem of this research is therefore to identify which AI-powered customer service factors most strongly influence customer loyalty outcomes in smart service ecosystems.

### 1.2 Research Objectives

1. To identify key AI-powered customer service factors that affect customer trust and satisfaction.
2. To examine the roles of personalization, interaction quality, problem-solving ability, human-like interaction, and cultural adaptation.
3. To analyze how trust and satisfaction influence customer retention, long-term engagement, and loyalty intention.
4. To design and evaluate a system that integrates an AI customer service chatbot with loyalty-related communication and prediction.
5. To define and apply an evaluation plan using a chatbot benchmark, survey data, and a loyalty prediction model.

### 1.3 Research Questions

**Main RQ.** What AI-powered customer service factors most influence customer loyalty, retention, long-term engagement, and loyalty tier progression in smart service ecosystems?

- **RQ1.** How do AI chatbot service quality, personalization, interaction quality, and problem-solving ability influence customer trust and satisfaction?
- **RQ2.** How do human-like interaction, personalization, and cultural adaptation affect customer acceptance of AI-powered customer service?
- **RQ3.** How do customer trust and satisfaction influence loyalty outcomes such as retention, continued engagement, and loyalty intention?
- **RQ4.** How can customer behavioural data be used to predict loyalty retention and tier progression?
- **RQ5.** Does an AI-powered (retrieval-augmented) assistant outperform conventional customer-service baselines, and what metrics measure its effectiveness?

This study does not aim to propose a new AI model from scratch. Instead, it investigates how an existing AI model can be integrated into a domain-specific customer service system and evaluates its effectiveness in improving support quality, trust, satisfaction, and loyalty outcomes.

---

## 2. Related Work

### 2.1 AI Chatbots and Customer Experience

AI chatbots have become common in customer-facing service. Cheng and Jiang [1] showed that AI-driven chatbot gratifications influence user satisfaction, loyalty, and continued use, while perceived privacy risk can reduce user experience. Adam et al. [2] found that human-like chatbot design cues increase perceived social presence and user compliance. Ameen et al. [3] identified convenience, personalization, service quality, and trust as central to AI-enabled customer experience. Together these studies argue that AI customer service should be judged not only on technical performance but also on user-centered outcomes such as satisfaction, trust, and continued engagement.

### 2.2 AI Chatbots, Trust, Satisfaction, and Loyalty

Several studies connect chatbot factors with loyalty outcomes. Li et al. [4] showed that chatbot affordances improve customer experience and retention. Shahzad et al. [5] found that AI-chatbot service quality influences e-brand loyalty through chatbot user trust, experience, and electronic word of mouth. These findings position trust and satisfaction as key mediators: customers stay loyal when AI support is useful, reliable, personalized, and easy to interact with.

### 2.3 AI Methods and Generative AI Customer Service

Suhaili et al. [6] reviewed service chatbots and noted that many studies emphasize technical functions over loyalty outcomes. Ferraro et al. [7] described the paradoxes of generative AI service — personalization vs. privacy, automation vs. empathy, efficiency vs. reliability. Gao et al. [8] showed that chatbot problem-solving ability drives expectation confirmation, satisfaction, trust, and continued usage. These works support using an LLM-based assistant while explicitly measuring problem-solving, reliability, and customer perception.

### 2.4 Loyalty Programs and Loyalty Tier Progression

Loyalty-program research grounds the domain. Chen et al. [9] reviewed three decades of work showing loyalty programs influence retention, repeat purchase, relationship strength, and engagement. Zeng et al. [10] found that progress framing in multi-tier programs affects customer motivation and tier movement. These studies define loyalty outcomes beyond general satisfaction: retention, engagement, loyalty intention, reward behaviour, and tier progression.

### 2.5 Perceived Empathy, Local Context, and Human-AI Interaction

Markovitch et al. [11] emphasized perceived empathy, especially after negative outcomes. Ngo et al. [12] studied AI chatbot continuance intention among Generation Z in Vietnam, identifying service quality, customization, interaction, enjoyment, problem-solving, and satisfaction as drivers. Chau et al. [13] showed that AI-powered customer service influences user experience, satisfaction, continued use, and decision-making in e-commerce. These add empathy, Vietnam-specific evidence, and human-AI interaction perspectives.

### 2.6 Research Gap

Existing studies examine AI customer service and loyalty programs **separately**. Chatbot studies focus on satisfaction, continuance, compliance, or e-brand loyalty; loyalty-program studies focus on reward mechanisms, progress framing, and behaviour without AI service interactions. There is limited research that directly connects AI customer service factors with loyalty tier progression, long-term engagement, and measurable loyalty behaviour in a smart service ecosystem. This study addresses that gap by integrating insights from thirteen papers into a single research model and an evaluated system that links AI service quality, personalization, problem-solving, perceived empathy, and privacy risk with trust, satisfaction, retention, engagement, and loyalty tier progression.

---

## 3. Proposed System and Methodology

### 3.1 Research Model

The proposed model contains four groups of variables.

| Variable Group | Variables | Expected Role |
|---|---|---|
| AI customer service factors | Service quality, personalization, interaction quality, problem-solving ability, response usefulness, social presence | Independent |
| Risk and perception factors | Human-like interaction, cultural adaptation, reliability concern | Moderating / influencing |
| Mediating factors | Customer trust, satisfaction, customer experience | Mediating |
| Loyalty outcomes | Customer loyalty, retention, continued engagement, loyalty intention, loyalty tier progression | Dependent |

AI customer service factors are expected to positively influence trust and satisfaction, which in turn influence loyalty outcomes. Human-like interaction and cultural/context fit are expected to strengthen customer acceptance of AI service.

### 3.2 System Overview and Users

The proposed system is an AI-powered customer service platform for a smart service ecosystem. It supports customer inquiries, recommends services, explains promotions and loyalty benefits, collects feedback, and optionally predicts customer retention or loyalty-tier risk. Main users are: (1) customers of online/booking services; (2) service staff monitoring support; (3) business managers tracking satisfaction and loyalty; and (4) administrators managing FAQ content, promotions, and loyalty rules.

### 3.3 Main Features

| Feature | Description |
|---|---|
| Customer account management | Register, log in, view profile |
| AI customer service chatbot | Answers questions and provides service support |
| FAQ and knowledge base | Answers common questions from stored service information |
| Promotion and loyalty explanation | Explains rewards, vouchers, points, tier benefits |
| Personalized recommendation | Suggests services, promotions, or loyalty actions |
| Feedback collection | Collects satisfaction, trust, and usefulness ratings |
| Loyalty prediction module | Optionally predicts retention risk or tier progression |
| Dashboard | Shows chatbot usage, satisfaction, and loyalty indicators |

### 3.4 System Architecture

| Component | Description |
|---|---|
| Frontend | Customer interface, chatbot window, feedback forms, dashboard |
| Backend API | Requests, authentication, business logic, orchestration |
| Database | User profiles, service info, chatbot logs, feedback, points, tiers |
| AI Service | Runs the chatbot model or calls an external LLM API |
| Knowledge Base | FAQ, promotion rules, service descriptions, loyalty rules |
| Loyalty Prediction Module | Estimates retention/tier movement from behaviour + survey data |

**Data flow.** (1) A customer submits a request through the frontend. (2) The backend checks relevant customer and service information. (3) The AI service generates a response using the chatbot model and knowledge base. (4) The response returns to the customer. (5) The system logs the interaction, response time, and feedback. (6) If enabled, the prediction module processes behaviour and feedback data. (7) The dashboard displays service-quality, satisfaction, and loyalty indicators.

### 3.5 AI Model Integration

The study integrates existing models rather than training new ones. The **chatbot** is a retrieval-augmented assistant: it grounds answers on the knowledge base (FAQ, promotion, and loyalty rules) and can be implemented with an LLM API (e.g., Gemini Flash, GPT-4o-mini) or an open-source model. Inputs include the customer question, profile context, FAQ, service descriptions, and loyalty rules; outputs include the answer, a suggested service, a loyalty/promotion explanation, and a recommended next action, with an escalation path to human staff for complaints or sensitive cases. The optional **loyalty prediction module** uses classical machine-learning models (Logistic Regression, Random Forest, XGBoost) on behavioural features (interactions, purchase frequency, points, tier, chatbot usage, satisfaction, trust, complaints, recency) to output retention probability and loyalty risk.

### 3.6 Methodology

The study uses a design- and evaluation-oriented methodology in three phases: (1) **literature analysis** to identify constructs and the research gap; (2) **system design** of the AI customer service platform; and (3) **evaluation** through three experiments — a chatbot benchmark (E1), a public survey dataset analysis (E2), and a loyalty-prediction task (E3). E1 is run on a real LLM and a real knowledge base; E2 uses a verified public Mendeley Data survey on banking chatbot service quality; E3 uses synthetic customer records because real customer behavioural logs were unavailable in this academic setting. All scripts and processed outputs are reproducible.

---

## 4. Experimental Setup

Three reproducible experiments were run (`scripts/run_all.py`, fixed seeds; Python 3.13, scikit-learn 1.7, xgboost 3.3).

**E1 — Chatbot prototype evaluation.** Three systems were compared on a shared 12-entry knowledge base and 50 annotated scenarios (15 FAQ, 13 loyalty, 11 personalization, 11 escalation): **S1**, the proposed retrieval-augmented assistant built on a *real LLM* (Google `gemini-2.5-flash-lite`), which retrieves the top-3 KB entries with TF-IDF and prompts the model to answer only from the KB, escalate complaint/security cases, and personalize when the query references the customer's own context; **B1**, a rule-based keyword/intent bot; and **B2**, a TF-IDF top-1 keyword-search bot. Each scenario was annotated with its gold KB entry, escalation requirement, and personalization requirement. Metrics: accuracy, escalation-handling rate, an automated 1–5 usefulness rubric scored against ground truth, and real wall-clock response time. The full LLM answers were saved for optional human re-rating.

**E2 — Public survey dataset analysis.** E2 uses *Data on Banking Chatbot Service Quality* from Mendeley Data [14] (Version 4, DOI `10.17632/jsvbvgzkf8.4`, CC BY 4.0), a structured questionnaire dataset from Indian banking chatbot users. The raw file contains 737 responses and includes semantic understanding, human-AI collaboration, human-like interaction, continuous improvement, personalization, cultural adaptation, efficiency, customer value, satisfaction, trust, and customer loyalty. Missing values coded as 0 were converted to missing, and the original 1 = Strongly Agree to 5 = Strongly disagree scale was reverse-coded so higher values indicate more positive perceptions. Analysis: Cronbach's α, descriptive statistics, Pearson correlations, and standardized OLS regressions.

**E3 — Loyalty-retention prediction.** 1,000 simulated customers with nine behavioural features and a binary `will_retain_next_6m` target drawn from a known logistic process with noise (~67% retention). An 80/20 stratified split with 5-fold cross-validated grid search compared a majority-class baseline, Logistic Regression, Random Forest, and XGBoost on Accuracy, Precision, Recall, F1, and ROC-AUC.

---

## 5. Results

### 5.1 E1 — Chatbot Prototype vs. Baselines

S1 was run on the real Gemini API (`gemini-2.5-flash-lite`); B1 and B2 are the deterministic baselines.

**Table 1. Overall system comparison (50 scenarios).**

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

Over 50 scenarios the proposed assistant reached 88.0% accuracy and 3.98/5 usefulness versus 64–68% and ≤3.12 for both baselines — a 28–31% relative usefulness gain. Its largest, most consistent advantage is escalation: it detected all 11 complaint/security cases (100% vs. 45.5%/0%), politely routing them to a human, and it also led on loyalty explanations (92.3% vs. 76.9%). The LLM performed reasoning the baselines cannot: asked *"I have 1,200 points, how many more to reach Gold?"* it replied *"Gold needs 1,500 points, so you are 300 short,"* computing the gap from the grounded rule. The honest failure modes were personalization (63.6%) when the needed customer context was absent from the prompt — the model correctly asked a clarifying question rather than inventing an answer — and one over-escalated FAQ, the single reason escalation handling is 98% rather than 100%; over-escalation is a safer error than wrong automation. The trade-off is latency (11.46 s of real API time vs. <1 ms), the expected efficiency-versus-quality paradox of generative AI service [7]. (Figure: `figures/e1_system_comparison.png`.)

### 5.2 E2 — Public Survey Dataset (Mendeley Data)

E2 uses a verified public banking-chatbot survey dataset from Mendeley Data rather than simulated respondents. All constructs exceed the 0.70 reliability threshold (α = 0.749–0.903), as shown in Table 3.

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

The strongest correlations are Trust ↔ Customer Loyalty (r = 0.736), Satisfaction ↔ Customer Loyalty (r = 0.718), and Trust ↔ Satisfaction (r = 0.660). These relationships directly support the proposed pathway from trust and satisfaction to loyalty outcomes.

**Table 4. OLS regression results** (standardized predictors; *** p<0.001, ** p<0.01, * p<0.05).

*Model 1 — Trust ~ chatbot service factors (N = 645, R² = 0.095)*

| Predictor | β | p | |
|---|---:|---:|---|
| Semantic Understanding | 0.170 | 0.0008 | *** |
| Human-AI Collaboration | −0.019 | 0.741 | ns |
| Human-Like Interaction | −0.069 | 0.213 | ns |
| Continuous Improvement | 0.029 | 0.599 | ns |
| Personalization | 0.003 | 0.962 | ns |
| Cultural Adaptation | 0.175 | 0.0013 | ** |
| Efficiency | 0.062 | 0.194 | ns |

*Model 2 — Satisfaction ~ chatbot service factors + Customer Value (N = 640, R² = 0.107)*

| Predictor | β | p | |
|---|---:|---:|---|
| Semantic Understanding | 0.180 | 0.0005 | *** |
| Human-AI Collaboration | −0.045 | 0.421 | ns |
| Human-Like Interaction | −0.028 | 0.614 | ns |
| Continuous Improvement | −0.063 | 0.253 | ns |
| Personalization | 0.055 | 0.314 | ns |
| Cultural Adaptation | 0.140 | 0.011 | * |
| Efficiency | −0.014 | 0.764 | ns |
| Customer Value | 0.139 | 0.0065 | ** |

*Model 3 — Customer Loyalty ~ Trust + Satisfaction + Customer Value (N = 644, R² = 0.649)*

| Predictor | β | p | |
|---|---:|---:|---|
| Trust | 0.440 | <0.001 | *** |
| Satisfaction | 0.424 | <0.001 | *** |
| Customer Value | 0.053 | 0.032 | * |

Semantic understanding and cultural adaptation significantly increase Trust and Satisfaction, while Trust and Satisfaction are the dominant predictors of Customer Loyalty (Model 3, R² = 0.649). This supports RQ1–RQ3 using a verified public survey dataset. (Figure: `figures/e2_external_correlation_heatmap.png`.)

### 5.3 E3 — Loyalty-Retention Prediction (n = 1,000)

**Table 5. Model comparison on the held-out test set.**

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Baseline (majority) | 0.670 | 0.670 | 1.000 | 0.802 | 0.500 |
| **Logistic Regression** | **0.770** | **0.779** | 0.918 | **0.843** | **0.806** |
| Random Forest | 0.755 | 0.767 | 0.910 | 0.833 | 0.799 |
| XGBoost | 0.720 | 0.753 | 0.866 | 0.806 | 0.761 |

All learned models beat the majority baseline on discriminative power: the baseline's F1 (0.802) is inflated by labelling everyone "retain," but its ROC-AUC of 0.500 shows no discrimination. Logistic Regression performed best (F1 0.843, AUC 0.806), consistent with the approximately logistic data process and showing a simple, interpretable model suffices (RQ4). Random-Forest feature importance ranked average satisfaction, average trust, recency, and purchase frequency highest — the same constructs E2 links to loyalty, giving cross-experiment convergence. (Figures: `figures/e3_roc_curve.png`, `figures/e3_feature_importance.png`.)

### 5.4 Cross-Experiment Synthesis

The experiments triangulate the central claim: E1 shows a real-LLM assistant delivers better service on the hard, loyalty-relevant interactions; E2 shows, using a verified public survey dataset, that trust and satisfaction strongly drive customer loyalty; E3 shows the behavioural signals of trust, satisfaction, engagement, and recency predict retention, enabling proactive intervention. Together they support the framework: **AI service quality → trust / satisfaction → loyalty outcomes**, with an operational prediction layer.

---

## 6. Discussion

This research contributes to both AI customer service and loyalty-program research. From the AI service perspective, the results confirm that chatbot effectiveness should be measured not only by speed or accuracy but by trust, satisfaction, human-like service quality, and loyalty: in E1 the real-LLM assistant matched the baselines on plain FAQ but pulled clearly ahead on escalation (100% vs. 45.5%/0%) and loyalty explanations, the interactions most relevant to retention, and in E2 trust and satisfaction were the strongest predictors of customer loyalty. This aligns with Shahzad et al. [5] and Gao et al. [8], who position trust and problem-solving as central mediators, and with Markovitch et al. [11] on the importance of empathy and escalation in negative-outcome situations.

From the loyalty-program perspective, the study extends the discussion from reward design and progress framing [9, 10] to AI-powered communication and prediction. The E3 prediction module shows that the same constructs surfaced in the survey (satisfaction, trust, engagement, recency) are operationally predictive of retention, so an AI service platform can not only react to inquiries but proactively flag at-risk customers and personalize loyalty communication — for example explaining how many points a customer needs to reach the next tier. The literature still warns that personalization must be paired with transparent data handling because privacy risk can damage customer trust [1, 7].

**Limitations.** E1 uses a real LLM on a real knowledge base, but its usefulness is scored with an automated rubric rather than human raters (the full LLM answers are saved for optional human re-rating), and the 50-scenario benchmark may not reflect the full distribution of real customer queries. E2 uses a verified public dataset, but it is secondary data from the banking domain in India, so the findings may not generalize to all smart service ecosystems and do not directly measure privacy risk. E3 uses synthetic customers, so it validates the prediction pipeline and expected relationships but not external generalizability. Survey-based loyalty may also diverge from actual future behaviour.

---

## 7. Conclusion and Future Work

This research proposes and evaluates an AI-powered customer service framework for improving customer loyalty in smart service ecosystems. Drawing on thirteen related papers, it links AI service quality, personalization, problem-solving, human-like interaction, trust, satisfaction, retention, and loyalty tier progression, addressing the gap that prior work studies AI chatbots and loyalty programs separately. Across three reproducible experiments, the proposed real-LLM retrieval-augmented assistant outperformed rule-based and keyword baselines (88.0% vs. 64–68% accuracy; 3.98 vs. ≤3.12 usefulness; 98% escalation handling on 50 scenarios); the verified public survey dataset confirmed that trust and satisfaction strongly predict customer loyalty; and the prediction module reached F1 0.843 / AUC 0.806, well above baseline.

**Future work** should extend the real-LLM chatbot to a full deployment with real users: collect survey responses from users interacting with the live chatbot, gather real interaction logs and loyalty records, recruit human raters for usefulness with inter-rater reliability (Cohen's κ), and test whether the framework improves actual retention and tier progression in a real service context. Further work could also evaluate additional models and study fairness and privacy safeguards in personalization.

---

## References

[1] [[02_related_work/paper_summaries/paper_01|Paper 01]] - Y. Cheng and H. Jiang, "How Do AI-driven Chatbots Impact User Experience? Examining Gratifications, Perceived Privacy Risk, Satisfaction, Loyalty, and Continued Use," Journal of Broadcasting & Electronic Media, 2020. https://doi.org/10.1080/08838151.2020.1834296

[2] [[02_related_work/paper_summaries/paper_02|Paper 02]] - M. Adam, M. Wessel, and A. Benlian, "AI-based chatbots in customer service and their effects on user compliance," Electronic Markets, 2021. https://doi.org/10.1007/s12525-020-00414-7

[3] [[02_related_work/paper_summaries/paper_03|Paper 03]] - N. Ameen, A. Tarhini, A. Reppel, and A. Anand, "Customer experiences in the age of artificial intelligence," Computers in Human Behavior, 2021. https://doi.org/10.1016/j.chb.2020.106548

[4] [[02_related_work/paper_summaries/paper_04|Paper 04]] - C.-Y. Li, Y.-H. Fang, and Y.-H. Chiang, "Can AI chatbots help retain customers? An integrative perspective using affordance theory and service-domain logic," Technological Forecasting and Social Change, 2023. https://doi.org/10.1016/j.techfore.2023.122921

[5] [[02_related_work/paper_summaries/paper_05|Paper 05]] - M. F. Shahzad, S. Xu, X. An, and I. Javed, "Assessing the impact of AI-chatbot service quality on user e-brand loyalty through chatbot user trust, experience and electronic word of mouth," Journal of Retailing and Consumer Services, 2024. https://doi.org/10.1016/j.jretconser.2024.103940

[6] [[02_related_work/paper_summaries/paper_06|Paper 06]] - S. M. Suhaili, N. Salim, and M. N. Jambli, "Service chatbots: A systematic review," Expert Systems with Applications, 2021. https://doi.org/10.1016/j.eswa.2021.115461

[7] [[02_related_work/paper_summaries/paper_07|Paper 07]] - C. Ferraro, V. Demsar, S. Sands, M. Restrepo, and C. Campbell, "The paradoxes of generative AI-enabled customer service: A guide for managers," Business Horizons, 2024. https://doi.org/10.1016/j.bushor.2024.04.004

[8] [[02_related_work/paper_summaries/paper_08|Paper 08]] - J. Gao, A. P. Opute, C. Jawad, and M. Zhan, "The influence of artificial intelligence chatbot problem solving on customers' continued usage intention in e-commerce platforms: an expectation-confirmation model approach," Journal of Business Research, 2025. https://doi.org/10.1016/j.jbusres.2025.115423

[9] [[02_related_work/paper_summaries/paper_09|Paper 09]] - Y. Chen, T. Mandler, and L. Meyer-Waarden, "Three decades of research on loyalty programs: A literature review and future research agenda," Journal of Business Research, 2021. https://doi.org/10.1016/j.jbusres.2020.10.057

[10] [[02_related_work/paper_summaries/paper_10|Paper 10]] - K. J. Zeng, I. Y. Yu, M. X. Yang, and H. Chan, "Communication strategies for multi-tier loyalty programs: The role of progress framing," Tourism Management, 2022. https://doi.org/10.1016/j.tourman.2021.104478

[11] [[02_related_work/paper_summaries/paper_11|Paper 11]] - D. G. Markovitch, R. A. Stough, and D. Huang, "Consumer reactions to chatbot versus human service: An investigation in the role of outcome valence and perceived empathy," Journal of Retailing and Consumer Services, 2024. https://doi.org/10.1016/j.jretconser.2024.103921

[12] [[02_related_work/paper_summaries/paper_12|Paper 12]] - T. T. A. Ngo, T. Y. N. Phan, T. K. Nguyen, N. B. T. Le, N. T. A. Nguyen, and T. T. D. Le, "Understanding continuance intention toward the use of AI chatbots in customer service among Generation Z in Vietnam," Acta Psychologica, 2025. https://doi.org/10.1016/j.actpsy.2025.105235

[13] [[02_related_work/paper_summaries/paper_13|Paper 13]] - H. K. L. Chau, T. T. A. Ngo, C. T. Bui, and N. P. N. Tran, "Human-AI interaction in E-Commerce: The impact of AI-powered customer service on user experience and decision-making," Computers in Human Behavior Reports, 2025. https://doi.org/10.1016/j.chbr.2025.100710

[14] P. Purushotham, "Data on Banking Chatbot Service Quality," Mendeley Data, Version 4, 2024. https://doi.org/10.17632/jsvbvgzkf8.4
