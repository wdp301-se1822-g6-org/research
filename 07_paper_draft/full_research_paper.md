# AI-Powered Customer Service for Improving Customer Loyalty in Smart Service Ecosystems

## Obsidian Links

- Map: [[research_map|Research Map]]
- Source topic: [[01_topic_proposal/topic_proposal|Topic Proposal]]
- Related work: [[02_related_work/literature_review_matrix|Literature Review Matrix]]
- Problem and gap: [[03_problem_and_gap/problem_statement|Problem Statement]], [[03_problem_and_gap/research_gap|Research Gap]], [[03_problem_and_gap/research_questions|Research Questions]]
- Proposed system: [[04_proposed_system/system_overview|System Overview]], [[04_proposed_system/system_architecture|System Architecture]], [[04_proposed_system/ai_model_integration|AI Model Integration]], [[04_proposed_system/data_flow|Data Flow]]
- Methodology: [[05_methodology/methodology|Methodology]], [[05_methodology/dataset|Dataset]], [[05_methodology/baseline|Baseline]], [[05_methodology/evaluation_metrics|Evaluation Metrics]]
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

## Abstract

AI-powered customer service has become an important component of smart service ecosystems because customers increasingly expect fast, accurate, personalized, and convenient support. Prior studies show that AI chatbots and generative AI service tools can improve customer experience, satisfaction, trust, continuance intention, and e-brand loyalty through factors such as service quality, personalization, interaction quality, problem-solving ability, social presence, and perceived usefulness. However, the reviewed literature also highlights several risks, including privacy concerns, limited empathy, unreliable responses, and over-reliance on automation. Based on a review of thirteen related studies on AI chatbots, customer experience, customer retention, loyalty programs, multi-tier loyalty programs, and human-AI interaction, this study investigates how AI-powered customer service factors influence customer loyalty in smart service ecosystems. The proposed research model connects AI service quality, personalization, problem-solving ability, perceived empathy, and privacy risk with customer trust and satisfaction, which then affect customer retention, long-term engagement, and loyalty tier progression. This study does not aim to develop a new AI model from scratch; instead, it focuses on integrating an existing AI-powered chatbot and optional loyalty prediction module into a customer service platform. The expected contribution is a practical AI customer service framework that can support customer inquiries, personalize loyalty-related communication, improve service experience, and provide measurable indicators for evaluating loyalty outcomes. The study can help service providers understand which AI service factors are most important for strengthening customer relationships and designing smarter loyalty programs.

**Keywords:** AI-powered customer service, AI chatbot, customer loyalty, customer retention, trust, satisfaction, loyalty tier progression, smart service ecosystem.

## 1. Introduction

Digital service platforms have changed the way customers interact with businesses. Customers now expect service providers to offer quick responses, accurate information, personalized recommendations, and convenient support across multiple digital channels. In this context, customer service is no longer only a support function. It has become an important part of customer experience and customer relationship management.

Traditional customer service often depends heavily on human staff. This approach can create several problems, such as slow response time, inconsistent service quality, limited personalization, and high operating cost. AI-powered customer service, especially chatbot-based support, can help address these limitations by answering customer questions, explaining promotions, recommending suitable services, supporting booking or purchasing decisions, and collecting customer feedback. With the development of large language models and generative AI, customer service chatbots can also provide more natural and context-aware interactions.

Customer loyalty is important because retaining existing customers is usually more cost-effective than acquiring new customers. In smart service ecosystems, customer loyalty may appear through repeated usage, continued engagement, positive word of mouth, reward redemption, and loyalty tier progression. However, businesses still need to understand which AI-powered service factors can actually support loyalty-related outcomes.

Previous studies have examined AI chatbots from different perspectives, including user experience, satisfaction, trust, continued usage intention, e-brand loyalty, customer retention, perceived empathy, privacy risk, and human-AI interaction. Studies on loyalty programs have also shown that reward design, engagement mechanisms, tier benefits, and progress framing can influence customer behavior. However, the connection between AI-powered customer service and loyalty tier progression is still limited. Therefore, this research investigates how AI customer service factors can influence customer trust, satisfaction, retention, long-term engagement, and movement across loyalty tiers in smart service ecosystems.

## 2. Problem Statement

In modern smart service ecosystems, customers expect service providers to respond quickly, accurately, and personally across digital channels. Traditional customer service is often limited by human staff availability, inconsistent response quality, long waiting time, and difficulty in providing personalized support for each customer. AI-powered customer service, especially chatbot-based support, can help service providers answer frequent questions, explain promotions, recommend services, support booking or purchasing decisions, and collect customer feedback more efficiently.

However, improving service efficiency alone is not enough. Businesses also need to understand whether AI-powered customer service can strengthen customer loyalty, retention, long-term engagement, and movement across loyalty tiers. Previous studies have shown that chatbot service quality, personalization, interaction, trust, satisfaction, empathy, and problem-solving ability can affect customer experience and continued usage intention. At the same time, privacy risk, lack of empathy, and unreliable responses may reduce customer trust and satisfaction.

Therefore, the main problem of this research is to identify which AI-powered customer service factors most strongly influence customer loyalty outcomes in smart service ecosystems. The study focuses on how an AI customer service chatbot, combined with loyalty-related communication and optional loyalty prediction, can support better customer experience and improve loyalty-related behavior.

## 3. Research Objectives

The main objective of this study is to investigate how AI-powered customer service can improve customer loyalty in smart service ecosystems.

The specific objectives are:

1. To identify key AI-powered customer service factors that affect customer trust and satisfaction.
2. To examine the roles of personalization, interaction quality, problem-solving ability, perceived empathy, and privacy risk in AI customer service.
3. To analyze how trust and satisfaction influence customer retention, long-term engagement, and loyalty intention.
4. To propose a system model that integrates an AI-powered customer service chatbot with loyalty-related communication.
5. To define an evaluation plan using survey data, system metrics, and optional behavioral or simulated loyalty data.

## 4. Research Questions

### 4.1 Main Research Question

What AI-powered customer service factors most influence customer loyalty, customer retention, long-term engagement, and loyalty tier progression in smart service ecosystems?

### 4.2 Sub Research Questions

RQ1. How do AI chatbot service quality, personalization, interaction quality, and problem-solving ability influence customer trust and satisfaction?

RQ2. How do perceived empathy and privacy risk affect customer acceptance of AI-powered customer service?

RQ3. How do customer trust and satisfaction influence loyalty outcomes such as retention, continued engagement, and loyalty intention?

RQ4. How can AI-powered customer service be integrated with loyalty program communication to support customer movement across loyalty tiers?

RQ5. What evaluation metrics can be used to measure the effectiveness of the proposed AI-powered customer service system?

## 5. Literature Review

### 5.1 AI Chatbots and Customer Experience

AI chatbots have become a common technology in customer-facing service environments. Cheng and Jiang [1] showed that AI-driven chatbot gratifications can influence user satisfaction, loyalty, and continued use, while perceived privacy risk can negatively affect user experience. Adam et al. [2] found that human-like chatbot design cues can increase perceived social presence and user compliance in customer service interactions. Ameen et al. [3] examined AI-enabled customer experience and identified factors such as convenience, personalization, service quality, and trust.

These studies suggest that AI-powered customer service should not be evaluated only by technical performance. It should also be evaluated through user-centered outcomes such as satisfaction, trust, perceived usefulness, and continued engagement.

### 5.2 AI Chatbots, Trust, Satisfaction, and Loyalty

Several studies directly connect chatbot service factors with loyalty-related outcomes. Li et al. [4] examined whether AI chatbots can help retain customers and showed that chatbot affordances can improve customer experience and retention. Shahzad et al. [5] found that AI-chatbot service quality can influence e-brand loyalty through chatbot user trust, user experience, and electronic word of mouth.

These findings indicate that customer trust and satisfaction are important mediating factors. Customers are more likely to continue using a service and remain loyal when AI support is useful, reliable, personalized, and easy to interact with.

### 5.3 AI Methods and Generative AI Customer Service

Suhaili et al. [6] reviewed service chatbot research and showed that chatbots have been applied across many domains, although many studies focus more on technical functions than broader customer loyalty outcomes. Ferraro et al. [7] discussed generative AI-enabled customer service and highlighted important paradoxes, including the balance between personalization and privacy, automation and empathy, and efficiency and reliability. Gao et al. [8] showed that chatbot problem-solving ability can influence expectation confirmation, satisfaction, trust, and continued usage intention.

These studies support the use of an LLM-based chatbot or AI customer support module in the proposed system. They also show that problem-solving ability, reliability, and customer perception should be included in the evaluation.

### 5.4 Loyalty Programs and Loyalty Tier Progression

Loyalty program research provides the domain foundation for this study. Chen et al. [9] reviewed three decades of loyalty program research and showed that loyalty programs can influence customer retention, repeat purchase, relationship strength, and engagement. Zeng et al. [10] examined multi-tier loyalty programs and found that progress framing can influence customer motivation and response toward loyalty tier movement.

These studies are important because they help define loyalty outcomes beyond general satisfaction. In this research, loyalty outcomes include customer retention, continued engagement, loyalty intention, reward-related behavior, and loyalty tier progression.

### 5.5 Perceived Empathy, Local Context, and Human-AI Interaction

Markovitch et al. [11] compared chatbot and human service and emphasized the role of perceived empathy, especially when service outcomes are negative. Ngo et al. [12] studied AI chatbot continuance intention among Generation Z in Vietnam and identified factors such as service quality, customization, interaction, enjoyment, problem-solving, satisfaction, and continuance intention. Chau et al. [13] examined human-AI interaction in e-commerce and showed that AI-powered customer service can influence user experience, satisfaction, continued use, and decision-making.

These supporting studies are useful for the proposed research because they add empathy, Vietnam-related evidence, and human-AI interaction perspectives to the model.

## 6. Research Gap

Existing studies have examined AI chatbots and AI-powered customer service from several important perspectives, including user experience, satisfaction, trust, social presence, service quality, continued usage intention, e-brand loyalty, customer retention, and human-AI interaction. Several studies show that chatbot quality, personalization, interaction quality, problem-solving ability, perceived usefulness, and perceived empathy can improve satisfaction, trust, and continued use. Other studies on loyalty programs show that reward design, customer engagement, communication strategy, progress framing, and tier-based benefits can influence customer retention and loyalty behavior.

However, most existing studies still examine AI customer service and loyalty programs separately. AI chatbot studies often focus on satisfaction, continuance intention, compliance, or e-brand loyalty, while loyalty program studies often focus on reward mechanisms, progress framing, and customer behavior without considering AI-powered customer service interactions. There is limited research that directly connects AI customer service factors with loyalty tier progression, long-term engagement, and measurable loyalty behavior in a smart service ecosystem.

This creates a research gap for the group: current literature does not sufficiently explain how AI-powered customer service can support customers not only in solving immediate service problems but also in developing trust, satisfaction, retention, and progression toward higher loyalty tiers. To address this gap, the proposed study integrates insights from thirteen related papers and develops a research model linking AI service quality, personalization, problem-solving ability, perceived empathy, and privacy risk with trust, satisfaction, customer retention, long-term engagement, and loyalty tier progression.

## 7. Proposed Research Model

The proposed research model contains four groups of variables.

| Variable Group | Variables | Expected Role |
|---|---|---|
| AI customer service factors | Service quality, personalization, interaction quality, problem-solving ability, response usefulness, social presence | Independent variables |
| Risk and perception factors | Privacy risk, perceived empathy, reliability concern | Moderating or influencing factors |
| Mediating factors | Customer trust, customer satisfaction, customer experience | Mediating variables |
| Loyalty outcomes | Customer loyalty, retention, continued engagement, loyalty intention, loyalty tier progression | Dependent variables |

The expected relationship is that AI customer service factors positively influence trust and satisfaction. Trust and satisfaction then influence loyalty-related outcomes. Privacy risk is expected to negatively affect trust and satisfaction, while perceived empathy is expected to strengthen customer acceptance of AI-powered customer service.

## 8. Proposed System

### 8.1 System Overview

The proposed system is an AI-powered customer service platform for a smart service ecosystem. The system supports customer inquiries, provides service recommendations, explains promotions and loyalty benefits, collects customer feedback, and optionally predicts customer loyalty or retention risk based on customer behavior.

### 8.2 Main Users

The main users include:

1. Customers who use online services or booking platforms.
2. Service staff who monitor customer support activities.
3. Business managers who want to understand customer satisfaction and loyalty.
4. Administrators who manage service information, FAQ content, promotions, and loyalty rules.

### 8.3 Main Features

| Feature | Description |
|---|---|
| Customer account management | Allows customers to register, log in, and view basic profile information |
| AI customer service chatbot | Answers customer questions and provides service support |
| FAQ and knowledge base support | Uses stored service information to answer common questions |
| Promotion and loyalty explanation | Explains rewards, vouchers, points, and loyalty tier benefits |
| Personalized recommendation | Suggests suitable services, promotions, or loyalty actions |
| Feedback collection | Collects satisfaction, trust, and perceived usefulness ratings |
| Loyalty prediction module | Optionally predicts retention risk or loyalty tier progression |
| Dashboard | Displays chatbot usage, satisfaction scores, and loyalty indicators |

### 8.4 System Architecture

The proposed architecture includes the following components:

| Component | Description |
|---|---|
| Frontend | Provides customer interface, chatbot window, feedback forms, and dashboard |
| Backend API | Handles user requests, authentication, business logic, and communication between components |
| Database | Stores user profiles, service information, chatbot logs, feedback, loyalty points, and loyalty tiers |
| AI Service | Runs the chatbot model or calls an external LLM API |
| Knowledge Base | Stores FAQ, promotion rules, service descriptions, and loyalty program information |
| Loyalty Prediction Module | Uses behavioral and survey data to estimate retention or loyalty tier movement |

### 8.5 Data Flow

1. A customer submits a question or support request through the frontend.
2. The backend receives the request and checks relevant customer and service information.
3. The AI service generates a response using the chatbot model and knowledge base.
4. The response is returned to the customer through the chatbot interface.
5. The system records the interaction log, response time, and feedback rating.
6. If loyalty prediction is enabled, customer behavior and feedback data are processed by the prediction module.
7. The dashboard displays service quality indicators, satisfaction scores, and loyalty-related insights.

## 9. AI Model Integration

This study does not aim to train a completely new AI model from scratch. Instead, it focuses on integrating existing AI models into a customer service system.

### 9.1 Chatbot Model

The chatbot can be implemented using an existing large language model API or an open-source language model. The model receives customer questions and relevant context from the knowledge base, then generates a natural language response.

The chatbot input may include:

- Customer question
- Customer profile context
- FAQ information
- Service descriptions
- Promotion rules
- Loyalty program rules

The chatbot output may include:

- Answer to customer question
- Suggested service
- Promotion or loyalty benefit explanation
- Recommended next action

### 9.2 Loyalty Prediction Model

The optional loyalty prediction module can use machine learning models such as Logistic Regression, Decision Tree, Random Forest, or XGBoost. The model can predict whether a customer is likely to continue using the service, become inactive, or move to a higher loyalty tier.

Possible input features include:

- Number of service interactions
- Recent purchase or booking frequency
- Loyalty points
- Current loyalty tier
- Chatbot usage frequency
- Satisfaction score
- Trust score
- Complaint frequency
- Response usefulness rating

Possible outputs include:

- Retention probability
- Loyalty risk level
- Recommended loyalty action
- Predicted tier progression

## 10. Methodology

The study uses a design-oriented and evaluation-based methodology. First, the group reviews related papers to identify key variables and research gaps. Second, the group designs a proposed AI-powered customer service system. Third, the group defines evaluation metrics to measure chatbot quality, user perception, and loyalty-related outcomes.

### 10.1 Research Design

The research design includes three main phases:

1. Literature analysis: Review thirteen papers and identify key constructs related to AI-powered customer service and loyalty.
2. System design: Propose an AI customer service platform with chatbot support, loyalty communication, and optional loyalty prediction.
3. Evaluation plan: Define survey items, system metrics, baseline comparison, and expected outcomes.

### 10.2 Data Collection Plan

The study can use two types of data:

| Data Type | Description |
|---|---|
| Survey data | User responses about perceived service quality, personalization, trust, satisfaction, privacy risk, empathy, continuance intention, and loyalty intention |
| Behavioral or simulated data | Customer interaction logs, chatbot usage frequency, service usage history, loyalty points, loyalty tier, and reward redemption |

If real customer data is not available, the group can use simulated customer behavior logs for prototype evaluation. Survey data can be collected from students or users who interact with the prototype chatbot.

### 10.3 Survey Constructs

The survey can measure the following constructs:

| Construct | Example Measurement |
|---|---|
| AI service quality | The chatbot provides useful and accurate support |
| Personalization | The chatbot gives responses suitable for my needs |
| Problem-solving ability | The chatbot helps me solve my service problem |
| Perceived empathy | The chatbot response feels polite and considerate |
| Privacy risk | I am concerned about how my data is used |
| Trust | I trust the chatbot-supported service |
| Satisfaction | I am satisfied with the AI customer service experience |
| Continuance intention | I intend to continue using this AI customer service |
| Loyalty intention | I am likely to keep using this service provider |

## 11. Evaluation Plan

### 11.1 Baseline

The proposed AI-powered customer service system can be compared with:

1. Traditional customer service without AI support.
2. A rule-based chatbot with fixed answers.
3. A non-personalized FAQ search system.

### 11.2 Evaluation Metrics

| Metric | Meaning | Why Used |
|---|---|---|
| Response time | Time needed to answer a customer question | Measures service efficiency |
| Answer usefulness rating | User rating of chatbot answer usefulness | Measures perceived support quality |
| User satisfaction score | Survey score after interaction | Measures customer experience |
| Trust score | User trust toward AI-supported service | Measures acceptance of AI service |
| Continuance intention score | Intention to continue using the chatbot | Measures future usage intention |
| Loyalty intention score | Intention to remain with the service provider | Measures loyalty outcome |
| Accuracy | Correct prediction ratio for loyalty model | Measures prediction performance |
| Precision | Correct positive predictions among predicted positives | Useful for identifying likely loyal or at-risk customers |
| Recall | Correctly detected positive cases among actual positives | Useful for finding at-risk customers |
| F1-score | Balance between precision and recall | Measures classification quality |

### 11.3 Evaluation Procedure

1. Prepare a set of customer service scenarios and loyalty-related questions.
2. Let users interact with the AI chatbot prototype.
3. Collect chatbot logs, response time, and user feedback.
4. Ask users to complete a survey about service quality, personalization, trust, satisfaction, privacy risk, empathy, and loyalty intention.
5. Compare the AI chatbot with a rule-based chatbot or FAQ baseline.
6. If using a loyalty prediction model, evaluate prediction performance using Accuracy, Precision, Recall, and F1-score.

## 12. Expected Results

The study expects that AI-powered customer service will improve customer experience compared with traditional or rule-based support. The chatbot is expected to provide faster responses, more personalized support, and better explanation of loyalty benefits. The research model expects that service quality, personalization, interaction quality, and problem-solving ability will positively influence customer trust and satisfaction. Trust and satisfaction are expected to positively influence retention, continued engagement, and loyalty intention.

The study also expects that privacy risk and low perceived empathy may reduce trust and satisfaction. Therefore, the proposed system should include careful data handling, clear communication, polite responses, and escalation to human staff when the chatbot cannot solve a customer issue.

## 13. Discussion

This research contributes to both AI customer service research and loyalty program research. From the AI service perspective, it emphasizes that chatbot effectiveness should be measured not only by speed or answer accuracy but also by customer trust, satisfaction, perceived empathy, and loyalty intention. From the loyalty program perspective, it extends the discussion from reward design and progress framing to AI-powered communication and customer support.

The proposed system can help service providers understand how customers interact with AI support and how those interactions may influence loyalty behavior. For example, a chatbot can explain how many points a customer needs to reach the next tier, recommend suitable services or promotions, and encourage continued engagement through personalized communication.

However, the study also has limitations. If real customer behavior data is unavailable, simulated data may not fully represent real loyalty behavior. Survey-based intention may not always match actual future behavior. In addition, AI chatbot responses may vary depending on the model, knowledge base quality, and prompt design.

## 14. Conclusion

This research proposes an AI-powered customer service approach for improving customer loyalty in smart service ecosystems. Based on thirteen related papers, the study identifies important factors such as AI service quality, personalization, interaction quality, problem-solving ability, perceived empathy, privacy risk, trust, satisfaction, retention, and loyalty tier progression. The main research gap is that existing studies often examine AI chatbots and loyalty programs separately, while limited research directly connects AI-powered customer service with loyalty tier movement and long-term engagement.

The proposed system integrates an AI customer service chatbot with loyalty-related communication and optional loyalty prediction. The expected contribution is a practical framework for supporting customer inquiries, improving customer experience, and measuring loyalty-related outcomes. Future work should implement the prototype, collect user survey data, evaluate chatbot performance, and test whether AI-powered customer service can improve customer retention and loyalty tier progression in real service contexts.

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
