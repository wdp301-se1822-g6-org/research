# Experiment Execution Plan — Group 6 (SE1822)

> **Mục tiêu:** Trong ~1 tuần, nhóm phải tạo ra dữ liệu thực nghiệm để điền vào Section 5 (Results) của paper. Plan này bám sát checklist thầy Trương Long (README §16) — phải có baseline, dataset, metrics, và kết quả thực nghiệm/đánh giá chuyên gia.

> **Update:** E2 ban đầu dự kiến dùng survey tự thu thập hoặc dữ liệu mô phỏng. Bản kết quả hiện tại đã thay E2 bằng verified public survey dataset từ Mendeley Data: *Data on Banking Chatbot Service Quality*, DOI `10.17632/jsvbvgzkf8.4`. Xem `experimental_setup.md`, `results.md`, và `data/external/banking_chatbot_mendeley/SOURCE.md`.

---

## 1. Tổng quan 3 thí nghiệm

Nhóm sẽ chạy **3 thí nghiệm song song**, mỗi thí nghiệm trả lời một nhóm Research Question khác nhau:

| # | Tên thí nghiệm | Trả lời RQ | Output chính |
|---|---|---|---|
| **E1** | Chatbot prototype evaluation (so với 2 baselines) | RQ1, RQ5 | Bảng so sánh response time, accuracy, usefulness của 3 hệ thống |
| **E2** | User survey (n≥40) — Likert scale + interaction | RQ1, RQ2, RQ3 | Descriptive stats, Cronbach's alpha, correlation/regression |
| **E3** | Loyalty prediction model trên synthetic data | RQ4 | Bảng Accuracy/Precision/Recall/F1 của 3 ML models vs baseline |

→ Đủ "có kết quả thực nghiệm" + "có baseline" + "có dữ liệu giả lập hợp lý" theo checklist thầy.

---

## 2. Phân công thành viên

| Thành viên | MSSV | Vai trò chính | Thí nghiệm phụ trách |
|---|---|---|---|
| **Đinh Hoàng Kha** (Leader) | SE193633 | Điều phối, build chatbot scaffolding, ghép paper cuối | E1 (lead) |
| **Nguyễn Quốc Đoàn** | SE180466 | Phân tích thống kê survey | E2 (analysis) |
| **Trần Hữu Phước** | SE180579 | Build 2 baselines, chấm chatbot scenarios | E1 (baselines) |
| **Nguyễn Minh Châu** | SE180582 | Thiết kế & deploy Google Form, gọi người làm survey | E2 (data collection) |
| **Nguyễn Trần Minh Hưng** | SE193002 | Sinh dataset & train ML model | E3 (lead) |

---

## 3. Timeline 7 ngày

> Giả định Day 1 = hôm nhóm đọc plan này. Điều chỉnh ngày tuyệt đối theo deadline thật của thầy.

| Ngày | Việc cần xong cuối ngày | Người làm |
|---|---|---|
| **Day 1** | Setup repos + API keys (OpenAI/Gemini); draft survey questions; chốt 30 chatbot scenarios; design schema synthetic dataset | Cả nhóm họp 1h, sau đó chia việc |
| **Day 2** | (a) LLM chatbot v1 chạy được; (b) rule-based + keyword baselines chạy được; (c) Google Form đã publish; (d) synthetic dataset 1000 rows sinh xong | Kha, Phước, Châu, Hưng |
| **Day 3** | (a) Chạy 30 scenarios trên 3 hệ thống → log response time + raw answers; (b) bắt đầu gọi người làm survey (target 40+); (c) train ML model lần 1 | Phước, Châu, Hưng |
| **Day 4** | (a) 2 người (Kha + Phước) chấm chéo answer usefulness theo rubric; (b) survey đạt n≥40; (c) ML có kết quả 3 models | Kha, Phước, Châu, Hưng |
| **Day 5** | Đoàn chạy phân tích thống kê survey (SPSS hoặc Python); viết Section 5 Results + bảng/biểu đồ | Đoàn, Kha |
| **Day 6** | Viết Section 4 (Experimental Setup), 6 (Discussion); restructure full_research_paper.md đúng cấu trúc IMRaD; export PDF từ LaTeX | Kha + cả nhóm review |
| **Day 7** | Slide pptx; final review; commit + nộp | Cả nhóm |

---

## 4. Chi tiết Thí nghiệm E1 — Chatbot Prototype Evaluation

### 4.1. Hệ thống được so sánh

| Hệ thống | Mô tả | Người build |
|---|---|---|
| **S1 (Proposed)** | LLM chatbot (Gemini Flash / GPT-4o-mini) + knowledge base có FAQ + promotion + loyalty rules, dùng system prompt tiếng Việt | Kha |
| **B1 (Baseline rule-based)** | Cây quyết định if-else trên intent đơn giản (~15 intents) | Phước |
| **B2 (Baseline keyword search)** | TF-IDF / cosine similarity trên FAQ database, trả về top-1 | Phước |

### 4.2. Test scenarios (n=30)

Phân bố:
- 10 câu FAQ thuần (giờ mở cửa, chính sách đổi trả, ...)
- 8 câu giải thích loyalty/promotion ("Tôi cần bao nhiêu điểm để lên hạng Gold?")
- 6 câu hỏi cá nhân hóa ("Tôi vừa đặt dịch vụ X, có khuyến mãi nào không?")
- 6 câu phức tạp / cần escalate ("Tôi muốn khiếu nại")

→ File: `06_experiment_results/scenarios.json` — Phước viết sẵn 30 prompts.

### 4.3. Metrics

| Metric | Cách đo |
|---|---|
| **Response time** (giây) | Log `time.time()` trước & sau khi gọi |
| **Answer usefulness** (1–5) | 2 người chấm (Kha + Phước) theo rubric; lấy trung bình; nếu lệch ≥2 thì người thứ 3 phân xử |
| **Answer accuracy** (đúng/sai) | Binary: trả lời có đúng thông tin trong knowledge base không |
| **Escalation correctness** (đúng/sai) | Khi nào nên đẩy sang nhân viên thật |

### 4.4. Rubric chấm usefulness

| Điểm | Mô tả |
|---|---|
| 5 | Trả lời đúng, đầy đủ, lịch sự, có gợi ý hành động tiếp theo |
| 4 | Trả lời đúng, đủ ý chính, ngôn ngữ ổn |
| 3 | Trả lời đúng nhưng thiếu chi tiết hoặc dài dòng |
| 2 | Trả lời sai một phần hoặc lạc đề một phần |
| 1 | Trả lời sai hoàn toàn hoặc không có ích |

### 4.5. Output dự kiến

Bảng vào `results.md`:

```
| Hệ thống | Avg Response Time (s) | Avg Usefulness | Accuracy (%) | Escalation OK (%) |
| S1 (LLM)       | ... | ... | ... | ... |
| B1 (Rule)      | ... | ... | ... | ... |
| B2 (Keyword)   | ... | ... | ... | ... |
```

---

## 5. Chi tiết Thí nghiệm E2 — User Survey

### 5.1. Đối tượng & cỡ mẫu

- **n ≥ 40** sinh viên FPT (bạn bè cùng khóa, các nhóm khác trong lớp SE1822, group Zalo lớp). 50–60 thì càng tốt cho phân tích regression.
- Mỗi người: (1) chat thử với S1 trên 3 scenario cố định (~5 phút), (2) làm Google Form (~7 phút).

### 5.2. Cấu trúc Google Form

**Phần A — Demographics** (4 câu): tuổi, giới tính, tần suất dùng chatbot trước đây, đã từng dùng dịch vụ có loyalty program chưa.

**Phần B — Constructs** (mỗi construct 3 items, Likert 5-point: 1=Rất không đồng ý → 5=Rất đồng ý)

| Construct | Item ví dụ |
|---|---|
| **AI Service Quality** (SQ1–SQ3) | "Chatbot trả lời chính xác câu hỏi của tôi" |
| **Personalization** (PE1–PE3) | "Chatbot đưa ra phản hồi phù hợp với nhu cầu của tôi" |
| **Problem-solving** (PS1–PS3) | "Chatbot giúp tôi giải quyết được vấn đề" |
| **Perceived Empathy** (EM1–EM3) | "Phản hồi của chatbot có sự lịch sự và quan tâm" |
| **Privacy Risk** (PR1–PR3, reverse) | "Tôi lo ngại về cách dữ liệu của tôi được dùng" |
| **Trust** (TR1–TR3) | "Tôi tin tưởng dịch vụ có chatbot hỗ trợ này" |
| **Satisfaction** (SA1–SA3) | "Tôi hài lòng với trải nghiệm chatbot" |
| **Loyalty Intention** (LI1–LI3) | "Tôi có ý định tiếp tục dùng dịch vụ này" |

→ 8 constructs × 3 items = 24 câu Likert. Châu copy từ `methodology.md` (Section 10.3) và tinh chỉnh sang tiếng Việt.

**Phần C — Open-ended** (2 câu): điểm thích nhất / điểm cần cải thiện. Dùng cho phần Discussion.

### 5.3. Phân tích (Đoàn làm — Python + pandas)

1. **Descriptive stats**: mean, std cho mỗi construct
2. **Reliability**: Cronbach's α cho từng construct (cần ≥ 0.7)
3. **Correlation matrix**: Pearson giữa 8 constructs
4. **Regression**:
   - DV1 = Trust ~ SQ + PE + PS + EM + PR
   - DV2 = Satisfaction ~ SQ + PE + PS + EM + PR
   - DV3 = Loyalty Intention ~ Trust + Satisfaction
5. **Báo cáo**: β, p-value, R² cho mỗi mô hình

### 5.4. Output dự kiến

3 bảng vào `results.md`:
- Bảng descriptive + Cronbach's α
- Bảng correlation matrix
- Bảng regression results (3 models)

---

## 6. Chi tiết Thí nghiệm E3 — Loyalty Prediction Model

### 6.1. Dataset (synthetic)

Hưng sinh **1000 customers** bằng Python + numpy, với features:

| Feature | Phân phối |
|---|---|
| `num_interactions` | Poisson(λ=15) |
| `purchase_frequency_per_month` | Gamma(2, 1.5) |
| `loyalty_points` | Normal(500, 200) |
| `current_tier` | Categorical: Bronze/Silver/Gold/Platinum (40/30/20/10%) |
| `chatbot_usage_freq` | Poisson(λ=5) |
| `avg_satisfaction_score` | Beta(5, 2) × 5 |
| `avg_trust_score` | Beta(4, 2) × 5 |
| `complaint_count_last_3m` | Poisson(λ=1) |
| `days_since_last_active` | Exponential(λ=1/30) |

**Target** (binary): `will_retain_next_6m` — quy luật sinh: hàm logistic của các features chính + nhiễu Gaussian, sao cho class imbalance ~ 70/30.

→ File `06_experiment_results/synthetic_dataset.csv` + script `generate_dataset.py`.

### 6.2. Models

| Model | Hyperparameter tuning |
|---|---|
| **Baseline** | Always predict majority class (no ML) |
| **Logistic Regression** | C ∈ {0.1, 1, 10} (GridSearchCV) |
| **Random Forest** | n_estimators ∈ {50, 100, 200} |
| **XGBoost** | max_depth ∈ {3, 5, 7} |

Train/test split: 80/20 stratified. 5-fold CV trên train set.

### 6.3. Metrics

Accuracy, Precision, Recall, F1-score, ROC-AUC (cho positive class = "will retain").

### 6.4. Output dự kiến

```
| Model        | Accuracy | Precision | Recall | F1 | ROC-AUC |
| Baseline     | ... | ... | ... | ... | ... |
| LogReg       | ... | ... | ... | ... | ... |
| RandomForest | ... | ... | ... | ... | ... |
| XGBoost      | ... | ... | ... | ... | ... |
```

Thêm 1 biểu đồ ROC curve so sánh 3 models → `figures/roc_curve.png`.

---

## 7. Deliverables checklist

Cuối tuần, các file sau phải tồn tại:

- [ ] `06_experiment_results/experimental_setup.md` — mô tả formal của 3 thí nghiệm (rút gọn từ plan này, dùng cho Section 4 paper)
- [ ] `06_experiment_results/results.md` — bảng kết quả + diễn giải (Section 5 paper)
- [ ] `06_experiment_results/scenarios.json` — 30 test prompts của E1
- [ ] `06_experiment_results/survey_responses.csv` — raw data từ Google Form
- [ ] `06_experiment_results/synthetic_dataset.csv` — data cho E3
- [ ] `06_experiment_results/figures/` — ít nhất 3 figure: bar chart so sánh chatbot, correlation heatmap survey, ROC curve
- [ ] `06_experiment_results/tables/` — file .csv hoặc .md cho mỗi bảng
- [ ] `07_paper_draft/full_research_paper.md` — **restructure lại** theo đúng cấu trúc thầy yêu cầu (xem §8 bên dưới)
- [ ] `08_final_submission/final_paper.pdf` — export từ LaTeX
- [ ] `08_final_submission/presentation.pptx`

---

## 8. Restructure paper — bỏ section thừa, thêm section thiếu

Cấu trúc hiện tại của `full_research_paper.md` có 14 section + nhiều section dạng proposal. Phải gộp/cắt về đúng template thầy (README §11):

| Section template thầy | Lấy từ section hiện tại |
|---|---|
| Title + Abstract + Keywords | Giữ nguyên |
| **1. Introduction** | Gộp current §1 Introduction + §2 Problem Statement + §3 Research Objectives + §4 Research Questions |
| **2. Related Work** | Giữ current §5 Literature Review + thêm 1 đoạn cuối tóm tắt research gap (lấy từ §6) |
| **3. Proposed System / Methodology** | Gộp current §7 Research Model + §8 Proposed System + §9 AI Model Integration + §10 Methodology |
| **4. Experimental Setup** | **VIẾT MỚI** từ §11 Evaluation Plan + chi tiết E1/E2/E3 ở plan này |
| **5. Results** | **VIẾT MỚI** — sau khi chạy 3 thí nghiệm |
| **6. Discussion** | Mở rộng current §13 Discussion với kết quả thực tế + so sánh với findings của các paper [1]–[13] |
| **7. Conclusion and Future Work** | Giữ current §14 Conclusion + thêm future work |
| References | Giữ nguyên |

→ **Xóa** các section dạng proposal: "Research Objectives" (gộp vào Intro), "Expected Results" (thay bằng Results thật).

---

## 9. Risk & fallback

| Rủi ro | Fallback |
|---|---|
| Không gọi được 40 người làm survey | Hạ target xuống n=25, không chạy regression mà chỉ correlation + descriptive |
| LLM API hết quota | Dùng Gemini Flash free tier; hoặc Ollama local với Llama 3.1 8B |
| ML model overfit synthetic data | Thừa nhận limitation trong Discussion: "synthetic data, future work needs real customer data" |
| 2 chấm viên lệch nhiều | Cộng thêm 1 người chấm thứ 3 (Châu); tính Cohen's kappa cho inter-rater agreement |

---

## 10. Bước tiếp theo (hôm nay)

1. **Họp nhóm 60 phút** — review plan này cùng nhau, chốt API nào dùng (Gemini hay GPT), ai trả tiền nếu cần
2. **Kha** tạo branch `experiments` và push plan này
3. Mỗi thành viên tạo 1 task theo phân công ở §2, commit Day 1 deliverables trước hôm sau
4. Báo cáo ngắn cuối Day 3 (qua chat nhóm) để Leader điều chỉnh nếu lệch tiến độ
