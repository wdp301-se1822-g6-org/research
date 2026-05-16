# Danh sách bài báo hội thảo tương tự: Ứng dụng AI Model vào hệ thống quản lý / hỗ trợ quyết định

## 1. Mục tiêu tìm bài tương tự

Mục tiêu của danh sách này là tìm các bài báo có dạng tương tự với ý tưởng:

> Xây dựng một ứng dụng quản lý hoặc hệ thống hỗ trợ quyết định, sau đó tích hợp một model AI đã có vào hệ thống để giải quyết một bài toán trong lĩnh vực cụ thể.

Dạng bài này thường không nhất thiết phải đề xuất model AI hoàn toàn mới. Thay vào đó, đóng góp chính nằm ở:

- Thiết kế hệ thống ứng dụng AI trong domain cụ thể.
- Tích hợp model AI vào quy trình quản lý hoặc hỗ trợ quyết định.
- Xây dựng pipeline dữ liệu và kiến trúc triển khai.
- Đánh giá hiệu quả của model AI trong ngữ cảnh ứng dụng.
- So sánh với quy trình thủ công, rule-based system, hoặc hệ thống không có AI.

---

## 2. Nhóm AI trong giáo dục / LMS / quản lý học tập

| STT | Tên bài báo | Loại / nguồn | Điểm giống với hướng nghiên cứu | Có thể học được gì |
|---|---|---|---|---|
| 1 | AI-Powered Quiz Generation for Learning Management Systems: A Full-Stack Implementation for Canvas LMS | CEUR Workshop Proceedings, 2025 | Xây dựng hệ thống full-stack tích hợp AI/NLP vào LMS để tự động sinh câu hỏi | Cách viết bài dạng system paper: có app, có AI module, có integration vào LMS |
| 2 | Aduvia: A Multi-Purpose AI-Powered Learning Management System (LMS) | NILES 2025 Conference | LMS tích hợp AI để hỗ trợ học tập, quản lý và tương tác với người dùng | Cách định vị hệ thống là AI-powered LMS thay vì chỉ là web app |
| 3 | AI-Powered Academic Advising Using Large Language Models | Conference paper trong bối cảnh giáo dục | Dùng LLM để hỗ trợ tư vấn học thuật cho sinh viên | Gần với hướng AI advisor, AI supervision, AI hỗ trợ chọn đề tài |
| 4 | AI-Augmented Advising | Journal of Learning Analytics, 2025 | So sánh phản hồi của GPT-4 với cố vấn học thuật thật | Có thể tham khảo cách đánh giá AI so với expert/human advisor |

### Nhận xét

Nhóm bài này phù hợp nếu muốn viết bài theo hướng:

> AI-powered education management system

hoặc:

> AI-assisted student support / academic advising / LMS enhancement.

Nếu phát triển đề tài **AI-powered topic registration management system**, nhóm bài này có thể dùng trong phần **Related Work** để chứng minh rằng AI đã được ứng dụng trong LMS, advising và academic support.

---

## 3. Nhóm quản lý đề tài / gợi ý giảng viên / recommendation trong giáo dục

| STT | Tên bài báo | Loại / nguồn | Điểm giống với hướng nghiên cứu | Có thể học được gì |
|---|---|---|---|---|
| 1 | Research Supervisor Recommendation System Based on Topic Conformity | Research system paper | Dùng TF-IDF và cosine similarity để gợi ý giảng viên hướng dẫn dựa trên topic | Rất gần với hướng đăng ký đề tài + gợi ý supervisor |
| 2 | Research Supervisor Recommendation System Using a Hybrid Filtering Approach | ICAITech 2025 Conference Paper | Dùng hybrid filtering để gợi ý giảng viên hướng dẫn | Có thể dùng làm baseline nếu nâng cấp bằng embedding/RAG |
| 3 | RecAdvisor: Criteria-based Ph.D. Supervisor Recommendation | ACM Conference Proceedings | Gợi ý supervisor dựa trên nhiều tiêu chí: area, topic, title, abstract | Học cách thiết kế input và tiêu chí matching |
| 4 | Research Project Topic Recommender System Using Artificial Intelligence Technology | Web-based recommender system | Hỗ trợ sinh viên chọn topic final assignment bằng AI | Gần với hướng topic recommendation trong hệ thống đăng ký đề tài |
| 5 | Topic Recommendation with Article Metadata using Collaborative and Content-based Filtering on Author Activeness Profiling | ICADSE 2025 | Gợi ý thesis topic bằng collaborative/content-based filtering và metadata bài báo | Có thể tham khảo nếu muốn module topic recommendation mạnh hơn |

### Nhận xét

Đây là nhóm bài **gần nhất** với chủ đề đề xuất:

> Agentic RAG-Based Topic Registration Management System for Context-Aware Research Supervision in Higher Education

Điểm mới có thể phát triển:

| Bài trước | Hướng nâng cấp đề xuất |
|---|---|
| TF-IDF + cosine similarity | Semantic embedding + vector database |
| Hybrid filtering | Agentic RAG + LLM feedback |
| Supervisor recommendation đơn giản | Supervisor recommendation dựa trên topic, publication, expertise, workload |
| Topic matching | Topic quality assessment + duplicate detection + rubric-based feedback |
| Web-based system | Full workflow: student submission, AI review, supervisor suggestion, lecturer approval |

### Gap có thể khai thác

Các bài trước thường tập trung vào **recommendation**, chưa tập trung nhiều vào:

- Quy trình đăng ký đề tài hoàn chỉnh.
- AI đánh giá chất lượng đề cương.
- RAG dựa trên rubric và dữ liệu đề tài cũ.
- LLM sinh phản hồi cải thiện title, objective, methodology.
- Explainable recommendation cho sinh viên và giảng viên.
- Dashboard hỗ trợ hội đồng hoặc bộ môn ra quyết định.

---

## 4. Nhóm quản lý nông nghiệp / IoT / AI decision support

| STT | Tên bài báo | Loại / nguồn | Điểm giống với hướng nghiên cứu | Có thể học được gì |
|---|---|---|---|---|
| 1 | Smart Agriculture Management System Using Virtual IoT and AI Decision Support | System paper / applied AI | Hệ thống quản lý nông nghiệp dùng Virtual IoT và AI decision support | Gần với hướng quản lý nông trại + sensor giả lập + AI khuyến nghị |
| 2 | A Decision Support System with Machine Learning for Smart Farming | Conference paper / ICAIIT 2025 | ML-based decision support system cho smart farming | Tham khảo phần problem, architecture và evaluation |
| 3 | IoT-Based Smart Agriculture Monitoring System with AI-Powered Decision Support | System paper | Dùng ESP32, sensor và AI để hỗ trợ giám sát nông nghiệp | Gần với hướng AIoT agriculture system |
| 4 | Integrating Artificial Intelligence and Internet of Things (IoT) for Smart and Precision Agriculture | Review, 2024 | Tổng quan AI + IoT trong smart farming | Dùng làm Related Work nền để chứng minh bối cảnh và gap |

### Nhận xét

Nhóm bài này phù hợp nếu chọn hướng:

> AIoT-Based Farm Management System Using Agentic RAG for Explainable Agricultural Decision Support

hoặc:

> An AI-Enhanced Farm Management System Using IoT Sensor Data and RAG-Based Decision Support

Điểm mới có thể nhấn mạnh:

- Không chỉ hiển thị sensor dashboard.
- Có RAG đọc tài liệu nông nghiệp.
- Có AI Agent giải thích khuyến nghị.
- Có testcase cho missing data, sensor fault, conflicting sensor.
- Có đánh giá chất lượng khuyến nghị bởi chuyên gia.

### Metric đánh giá phù hợp

| Nhóm đánh giá | Metric |
|---|---|
| Phân loại trạng thái | Accuracy, Precision, Recall, F1-score |
| Khuyến nghị | Expert rating, relevance score, usefulness score |
| Hệ thống | Response time, uptime, data latency |
| Tình huống lỗi | Detection rate for missing/fault/conflicting sensors |
| Người dùng | User satisfaction, perceived explainability |

---

## 5. Nhóm quản lý kho / inventory / logistics

| STT | Tên bài báo | Loại / nguồn | Điểm giống với hướng nghiên cứu | Có thể học được gì |
|---|---|---|---|---|
| 1 | Smart Inventory Management System Using Machine Learning | Conference / system paper | Dùng Random Forest dự báo nhu cầu từ lịch sử bán hàng, kết hợp stock monitoring | Mẫu tốt cho bài management system + ML model + evaluation |
| 2 | Smart Inventory Management System with Real-Time Package Tracking Using Machine Learning | IEEE ICoECIT 2026 Conference | Quản lý tồn kho, tracking thời gian thực, dùng ML | Tham khảo nếu viết về warehouse/logistics management |
| 3 | Applications of Machine Learning in Supply Chain Management for Inventory Optimization | ACM ICMML 2025 Proceedings | Ứng dụng ML vào supply chain và inventory optimization | Dùng làm Related Work cho inventory optimization |
| 4 | Comparative Study of Machine Learning Techniques for Inventory Management | ACM Conference Proceedings, 2024 | So sánh các kỹ thuật ML cho inventory classification/management | Học cách làm benchmark model trong bài ứng dụng |

### Nhận xét

Nhóm này phù hợp nếu muốn viết bài theo hướng:

> Smart Warehouse Management System Using Machine Learning for Demand Forecasting and Inventory Recommendation

Ưu điểm:

- Dễ có metric định lượng.
- Dễ so sánh model.
- Dễ viết phần experimental setup.
- Có thể dùng public dataset.

Hạn chế:

- Có thể hơi xa với thế mạnh hiện tại nếu đang tập trung vào giáo dục, RAG hoặc AI Agent.
- Cần dữ liệu bán hàng/kho đủ tốt để đánh giá.

### Metric đánh giá phù hợp

| Bài toán | Metric |
|---|---|
| Dự báo nhu cầu | MAE, RMSE, MAPE |
| Phân loại sản phẩm | Accuracy, F1-score |
| Gợi ý nhập hàng | Stockout reduction, over-stock reduction |
| Vận hành hệ thống | Response time, processing time |
| Kinh doanh | Inventory turnover, cost saving estimate |

---

## 6. Nhóm y tế / mobile app tích hợp AI model

| STT | Tên bài báo | Loại / nguồn | Điểm giống với hướng nghiên cứu | Có thể học được gì |
|---|---|---|---|---|
| 1 | Mobile Application for Skin Cancer Classification Using Deep Learning | Application paper | Mobile app tích hợp CNN/transfer learning để phân loại ung thư da | Ví dụ rõ về việc dùng pretrained model trong ứng dụng cụ thể |
| 2 | Mobile Application Using CNN for Skin Disease Classification with User Privacy | IEEE ICAICCIT 2023 Conference | App mobile dùng CNN phân loại bệnh da, có xét đến privacy | Cách trình bày app + model + privacy + evaluation |

### Nhận xét

Nhóm này chứng minh rằng một bài hội thảo có thể được xây dựng từ:

- Một ứng dụng thực tế.
- Một model AI đã có.
- Một dataset public.
- Một pipeline xử lý dữ liệu.
- Một phần đánh giá model.
- Một phần thảo luận về triển khai thực tế.

Tuy nhiên, nếu không có chuyên môn y tế hoặc dữ liệu phù hợp, nên chỉ dùng nhóm này làm ví dụ tham khảo, không nhất thiết chọn làm hướng chính.

---

## 7. Các bài nên ưu tiên đọc trước

| Ưu tiên | Tên bài | Lý do nên đọc |
|---|---|---|
| 1 | Research Supervisor Recommendation System Based on Topic Conformity | Gần nhất với hướng quản lý đăng ký đề tài và gợi ý giảng viên |
| 2 | Research Supervisor Recommendation System Using a Hybrid Filtering Approach | Có thể làm baseline để nâng cấp bằng embedding/RAG |
| 3 | RecAdvisor: Criteria-based Ph.D. Supervisor Recommendation | Học cách xây dựng tiêu chí matching nhiều chiều |
| 4 | AI-Powered Quiz Generation for Learning Management Systems | Mẫu tốt cho bài full-stack system tích hợp AI vào LMS |
| 5 | Aduvia: A Multi-Purpose AI-Powered Learning Management System | Mẫu tốt cho bài AI-powered management system trong giáo dục |
| 6 | Smart Agriculture Management System Using Virtual IoT and AI Decision Support | Phù hợp nếu chọn hướng AIoT agriculture |
| 7 | A Decision Support System with Machine Learning for Smart Farming | Có thể học cách viết bài decision support system |
| 8 | Smart Inventory Management System Using Machine Learning | Mẫu tốt cho bài management system + ML model + evaluation |

---

## 8. Đề xuất hướng bài có tiềm năng nhất

### Chủ đề đề xuất

> Agentic RAG-Based Topic Registration Management System for Context-Aware Research Supervision in Higher Education

### Vì sao hướng này tốt?

| Tiêu chí | Đánh giá |
|---|---|
| Gần domain giáo dục đại học | Rất cao |
| Dễ triển khai demo | Cao |
| Dễ lấy dữ liệu | Trung bình đến cao |
| Có bài nền liên quan | Có |
| Có thể tạo điểm mới | Cao |
| Có thể đánh giá định lượng | Có |
| Có thể đánh giá chuyên gia | Có |
| Phù hợp hội thảo | Cao |

### Điểm mới so với các bài tương tự

| Nhóm bài cũ | Hạn chế thường gặp | Điểm mới đề xuất |
|---|---|---|
| Supervisor recommendation | Chủ yếu matching bằng TF-IDF/cosine hoặc filtering | Dùng embedding, vector DB, RAG và LLM |
| Topic recommendation | Tập trung gợi ý topic, chưa quản lý workflow duyệt đề tài | Xây dựng hệ thống quản lý đăng ký đề tài đầy đủ |
| AI-powered LMS | Tập trung quiz/feedback học tập | Tập trung research supervision và topic approval |
| Academic advising | Tập trung tư vấn học vụ | Tập trung chọn đề tài, gợi ý supervisor, đánh giá proposal |
| Web-based recommender | Ít giải thích lý do gợi ý | Có explainable recommendation và rubric-based feedback |

---

## 9. Khung bài báo đề xuất

## Title

Agentic RAG-Based Topic Registration Management System for Context-Aware Research Supervision in Higher Education

## Abstract

Trình bày ngắn gọn:

- Vấn đề trong quy trình đăng ký đề tài.
- Hạn chế của duyệt thủ công và matching truyền thống.
- Hệ thống đề xuất sử dụng embedding, vector database, RAG và LLM.
- Cách đánh giá.
- Kết quả kỳ vọng hoặc kết quả thực nghiệm.

## 1. Introduction

- Bối cảnh đăng ký đề tài trong giáo dục đại học.
- Vấn đề: trùng đề tài, chọn sai giảng viên, đề cương mơ hồ, tốn thời gian duyệt.
- Lý do cần AI-assisted workflow.
- Đóng góp chính.

## 2. Related Work

Chia thành các nhóm:

1. AI-powered LMS.
2. Academic advising systems.
3. Research supervisor recommendation.
4. Topic recommendation systems.
5. RAG and LLM-based decision support.

## 3. Proposed System

Mô tả:

- Kiến trúc tổng quan.
- Dữ liệu đầu vào.
- Các module AI.
- Quy trình người dùng.
- Cách hệ thống giải thích kết quả.

## 4. Methodology

Các thành phần kỹ thuật:

- Data preprocessing.
- Embedding generation.
- Vector search.
- Duplicate detection.
- Supervisor recommendation.
- RAG-based feedback generation.
- Rubric-based topic evaluation.

## 5. Experimental Setup

Cần có:

- Dataset đề tài cũ.
- Hồ sơ giảng viên.
- Rubric đánh giá đề tài.
- Baseline: manual review, TF-IDF + cosine, hoặc LLM-only.
- Metrics.

## 6. Results

Có thể trình bày:

- Kết quả phát hiện đề tài trùng.
- Kết quả gợi ý giảng viên.
- Kết quả đánh giá feedback AI.
- Thời gian tiết kiệm so với quy trình thủ công.
- Đánh giá chuyên gia.

## 7. Discussion

Thảo luận:

- Hệ thống hỗ trợ giảng viên thế nào.
- Khi nào AI gợi ý sai.
- Rủi ro hallucination.
- Vấn đề dữ liệu riêng tư.
- Khả năng mở rộng sang capstone/thesis/project registration.

## 8. Conclusion and Future Work

Kết luận và hướng mở rộng:

- Graph-RAG.
- Student learning graph.
- Multi-agent workflow.
- Tích hợp LMS/SIS.
- Đánh giá trên dữ liệu nhiều học kỳ.

---

## 10. Câu định vị bài báo nên dùng

Có thể dùng câu sau trong Introduction hoặc Methodology:

> This study does not aim to propose a new AI model from scratch. Instead, it investigates how existing AI models, including semantic embedding and large language models, can be integrated into a domain-specific topic registration management system to support duplicate detection, supervisor recommendation, and rubric-based feedback generation.

Phiên bản tiếng Việt:

> Nghiên cứu này không nhằm đề xuất một mô hình AI hoàn toàn mới, mà tập trung khảo sát cách tích hợp các mô hình AI hiện có, bao gồm semantic embedding và large language model, vào một hệ thống quản lý đăng ký đề tài nhằm hỗ trợ phát hiện trùng lặp, gợi ý giảng viên hướng dẫn và sinh phản hồi dựa trên rubric.

---

## 11. Kết luận

Có nhiều bài báo tương tự chứng minh rằng hoàn toàn có thể viết bài hội thảo theo hướng:

> Ứng dụng một model AI đã có vào một hệ thống quản lý hoặc hỗ trợ quyết định trong domain cụ thể.

Trong các hướng đã khảo sát, hướng phù hợp nhất là:

> AI-Assisted Research Topic Registration and Supervisor Recommendation System

hoặc phiên bản mạnh hơn:

> Agentic RAG-Based Topic Registration Management System for Context-Aware Research Supervision in Higher Education

Đây là hướng có thể tận dụng các bài nền về:

- Supervisor recommendation.
- Topic recommendation.
- AI-powered LMS.
- Academic advising.
- RAG-based decision support.

Đồng thời vẫn có khoảng trống để phát triển điểm mới bằng:

- Semantic embedding thay cho TF-IDF.
- Vector database.
- RAG dựa trên đề tài cũ, hồ sơ giảng viên và rubric.
- LLM feedback cho proposal.
- Explainable supervisor recommendation.
- Workflow quản lý duyệt đề tài hoàn chỉnh.
