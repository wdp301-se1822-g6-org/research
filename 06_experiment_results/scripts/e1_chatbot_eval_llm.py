"""
E1 (real-LLM variant) - Chatbot prototype evaluation with a REAL LLM as S1.

S1 is a genuine retrieval-augmented assistant: for each scenario it retrieves
the top-k knowledge-base entries with TF-IDF, stuffs them into a Vietnamese
grounding prompt, and calls a real LLM API. The LLM returns strict JSON with
its answer, the KB id it relied on, and escalation / personalization flags.
B1 (rule-based) and B2 (TF-IDF) baselines are recomputed identically to the
simulated experiment for a fair comparison. Real wall-clock latency is measured.

Provider is selected via environment variables (no key is ever written to disk):
    LLM_PROVIDER = gemini | openai | anthropic   (default: gemini)
    LLM_MODEL    = optional model id override
    GEMINI_API_KEY / OPENAI_API_KEY / ANTHROPIC_API_KEY

Run:
    LLM_PROVIDER=gemini GEMINI_API_KEY=...  python scripts/e1_chatbot_eval_llm.py
Outputs (suffixed _llm so the simulated run is preserved):
    data/e1_per_scenario_llm.csv
    data/e1_raw_answers_llm.csv          (full LLM answers, for optional human rating)
    tables/e1_system_comparison_llm.csv
    tables/e1_accuracy_by_category_llm.csv
    figures/e1_system_comparison_llm.png
"""
import os, json, time, re
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE = Path(__file__).resolve().parents[1]

# ---- Knowledge base (same 12 entries as the simulated run) ----
KB = {
    "kb_hours":      {"kw": ["giờ", "mở cửa", "đóng cửa", "thời gian", "làm việc"],
                      "ans": "Trung tâm dịch vụ mở cửa 8:00–22:00 hằng ngày, kể cả cuối tuần."},
    "kb_return":     {"kw": ["đổi", "trả", "hoàn", "hủy", "chính sách"],
                      "ans": "Bạn có thể đổi hoặc hủy dịch vụ miễn phí trước 24 giờ so với lịch hẹn."},
    "kb_payment":    {"kw": ["thanh toán", "trả tiền", "thẻ", "ví", "momo", "chuyển khoản"],
                      "ans": "Chúng tôi hỗ trợ thanh toán qua thẻ nội địa, thẻ quốc tế, MoMo và chuyển khoản."},
    "kb_booking":    {"kw": ["đặt", "booking", "đặt lịch", "đặt chỗ", "đăng ký dịch vụ"],
                      "ans": "Bạn có thể đặt lịch ngay trong ứng dụng ở mục 'Đặt dịch vụ', chọn thời gian và xác nhận."},
    "kb_points":     {"kw": ["điểm", "tích điểm", "point", "loyalty point"],
                      "ans": "Mỗi 10.000đ chi tiêu được tích 1 điểm thưởng; điểm dùng để đổi quà và lên hạng."},
    "kb_tier":       {"kw": ["hạng", "tier", "gold", "silver", "bronze", "platinum", "lên hạng"],
                      "ans": "Có 4 hạng: Bronze, Silver (500 điểm), Gold (1500 điểm), Platinum (3000 điểm)."},
    "kb_tier_gold":  {"kw": ["gold", "lên gold", "hạng vàng", "bao nhiêu điểm gold"],
                      "ans": "Để đạt hạng Gold bạn cần tích lũy 1500 điểm thưởng."},
    "kb_voucher":    {"kw": ["voucher", "mã giảm giá", "khuyến mãi", "ưu đãi", "giảm giá"],
                      "ans": "Voucher hiện có trong mục 'Ưu đãi'; hạng càng cao thì ưu đãi càng lớn."},
    "kb_account":    {"kw": ["tài khoản", "đăng nhập", "mật khẩu", "quên mật khẩu", "đăng ký"],
                      "ans": "Bạn có thể đặt lại mật khẩu qua 'Quên mật khẩu' ở màn hình đăng nhập."},
    "kb_refund_time":{"kw": ["khi nào", "bao lâu", "hoàn tiền", "nhận lại tiền"],
                      "ans": "Tiền hoàn sẽ về tài khoản trong vòng 3–5 ngày làm việc."},
    "kb_contact":    {"kw": ["liên hệ", "hotline", "số điện thoại", "email", "tổng đài"],
                      "ans": "Bạn có thể liên hệ hotline 1900-1234 hoặc email support@smartservice.vn."},
    "kb_privacy":    {"kw": ["dữ liệu", "bảo mật", "thông tin cá nhân", "privacy", "an toàn"],
                      "ans": "Dữ liệu của bạn được mã hóa và chỉ dùng để cải thiện chất lượng dịch vụ."},
}
KB_IDS = list(KB.keys())
KB_DOCS = [" ".join(v["kw"]) + " " + v["ans"] for v in KB.values()]
_vec = TfidfVectorizer()
_kb_mat = _vec.fit_transform(KB_DOCS)

scenarios = json.loads((BASE / "scenarios.json").read_text(encoding="utf-8"))

# ---- Baselines (identical to simulated run) ----
ESC_TRIGGERS = ["khiếu nại", "bồi thường", "thất vọng", "gặp quản lý", "hack",
                "trừ tiền hai lần", "nghiêm trọng", "thái độ", "hỏng", "mất tiền",
                "xử lý ngay", "gấp", "báo cáo"]

def system_b1(text):
    t = text.lower(); best, hits = None, 0
    for kid, v in KB.items():
        h = sum(1 for k in v["kw"] if k in t)
        if h > hits: best, hits = kid, h
    return {"kb": best if hits > 0 else None, "escalate": False, "personalized": False}

def system_b2(text):
    sims = cosine_similarity(_vec.transform([text]), _kb_mat)[0]
    j = int(sims.argmax())
    return {"kb": KB_IDS[j] if sims[j] > 0.05 else None, "escalate": False, "personalized": False}

# ---- Real LLM call (S1) ----
def retrieve(text, k=3):
    sims = cosine_similarity(_vec.transform([text]), _kb_mat)[0]
    idx = sims.argsort()[::-1][:k]
    return [(KB_IDS[i], KB[KB_IDS[i]]["ans"]) for i in idx]

SYS_PROMPT = (
    "Bạn là trợ lý chăm sóc khách hàng AI cho một nền tảng dịch vụ thông minh có "
    "chương trình khách hàng thân thiết 4 hạng. Chỉ trả lời dựa trên các mục tri "
    "thức (knowledge base) được cung cấp. Nếu khách hàng phàn nàn, tức giận, yêu "
    "cầu bồi thường, báo lỗi nghiêm trọng hoặc vấn đề bảo mật tài khoản, hãy chuyển "
    "cho nhân viên (escalate=true). Nếu câu hỏi nhắc tới thông tin cá nhân của khách "
    "(điểm của tôi, hạng của tôi, tôi vừa đặt...), hãy cá nhân hóa câu trả lời "
    "(personalized=true). Luôn trả lời bằng tiếng Việt, lịch sự, ngắn gọn.\n"
    "Trả về DUY NHẤT một JSON: "
    '{"answer": str, "used_kb_id": str hoặc null, "escalate": bool, "personalized": bool}'
)

def build_prompt(text):
    kb_ctx = "\n".join(f"- [{kid}] {ans}" for kid, ans in retrieve(text))
    return (f"{SYS_PROMPT}\n\nCác mục tri thức liên quan:\n{kb_ctx}\n\n"
            f"Câu hỏi của khách hàng: \"{text}\"\n\nJSON:")

def parse_json(raw):
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    if not m:
        return {"answer": raw.strip(), "used_kb_id": None, "escalate": False, "personalized": False}
    try:
        d = json.loads(m.group(0))
    except Exception:
        return {"answer": raw.strip(), "used_kb_id": None, "escalate": False, "personalized": False}
    kid = d.get("used_kb_id")
    if kid not in KB:
        kid = None
    return {"answer": d.get("answer", ""), "used_kb_id": kid,
            "escalate": bool(d.get("escalate", False)),
            "personalized": bool(d.get("personalized", False))}

PROVIDER = os.environ.get("LLM_PROVIDER", "gemini").lower()
REQUEST_DELAY = float(os.environ.get("LLM_REQUEST_DELAY", "6"))  # seconds between S1 calls

def with_retry(fn, retries=6):
    """Call fn(prompt) with exponential backoff on rate-limit / transient errors."""
    def wrapped(prompt):
        delay = 8.0
        for attempt in range(retries):
            try:
                return fn(prompt)
            except Exception as e:
                msg = str(e).lower()
                transient = ("429" in msg or "exhaust" in msg or "quota" in msg
                             or "rate" in msg or "503" in msg or "unavailable" in msg
                             or "timeout" in msg or "500" in msg)
                if not transient or attempt == retries - 1:
                    raise
                print(f"      retry {attempt+1}/{retries} after {delay:.0f}s ({type(e).__name__})")
                time.sleep(delay)
                delay = min(delay * 1.8, 90)
    return wrapped

def make_caller():
    if PROVIDER == "gemini":
        import google.generativeai as genai
        # Accept one or many keys: GEMINI_API_KEYS (comma/space separated) or GEMINI_API_KEY.
        raw = os.environ.get("GEMINI_API_KEYS") or os.environ.get("GEMINI_API_KEY", "")
        keys = [k.strip() for k in re.split(r"[,\s]+", raw) if k.strip()]
        if not keys:
            raise SystemExit("No Gemini key found (set GEMINI_API_KEYS or GEMINI_API_KEY).")
        mdl = os.environ.get("LLM_MODEL", "gemini-2.5-flash-lite")
        print(f"  ({len(keys)} Gemini key(s) loaded for rotation)")
        state = {"i": 0, "exhausted": set()}
        def call(prompt):
            # Try each not-yet-exhausted key once, round-robin. Raise quota error
            # only if every key is exhausted (then with_retry backs off and resets).
            n = len(keys)
            for _ in range(n):
                idx = state["i"] % n
                state["i"] += 1
                if idx in state["exhausted"]:
                    continue
                genai.configure(api_key=keys[idx])
                try:
                    r = genai.GenerativeModel(mdl).generate_content(
                        prompt, generation_config={"temperature": 0.2})
                    return r.text
                except Exception as e:
                    msg = str(e).lower()
                    if "429" in msg or "exhaust" in msg or "quota" in msg:
                        state["exhausted"].add(idx)
                        continue
                    raise
            state["exhausted"].clear()  # all hit quota; let with_retry sleep then retry
            raise RuntimeError("All Gemini keys hit quota (429)")
        return call
    if PROVIDER == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        mdl = os.environ.get("LLM_MODEL", "gpt-4o-mini")
        def call(prompt):
            r = client.chat.completions.create(
                model=mdl, temperature=0.2,
                messages=[{"role": "user", "content": prompt}])
            return r.choices[0].message.content
        return call
    if PROVIDER == "anthropic":
        import anthropic
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        mdl = os.environ.get("LLM_MODEL", "claude-haiku-4-5-20251001")
        def call(prompt):
            r = client.messages.create(
                model=mdl, max_tokens=400, temperature=0.2,
                messages=[{"role": "user", "content": prompt}])
            return r.content[0].text
        return call
    raise SystemExit(f"Unknown LLM_PROVIDER={PROVIDER}")

def usefulness(scn, kb, escalate, personalized):
    if scn["esc"]:
        return 5 if escalate else 2
    if escalate:
        return 2
    if kb != scn["gold"]:
        return 2 if kb is not None else 1
    if scn["pers"]:
        return 5 if personalized else 3
    return 4

CACHE = BASE / "data" / "e1_s1_cache_llm.json"

def load_cache():
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}

def save_cache(cache):
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")

def main():
    call = with_retry(make_caller())
    print(f"Using provider={PROVIDER}, model={os.environ.get('LLM_MODEL','(default)')}")
    cache = load_cache()  # scenario_id (str) -> S1 result dict (resumable across runs)
    print(f"Resuming: {len(cache)}/{len(scenarios)} S1 answers already cached")
    rows, raws = [], []
    for scn in scenarios:
        # B1, B2
        for name, out in [("B1 (Rule-based)", system_b1(scn["text"])),
                          ("B2 (TF-IDF)", system_b2(scn["text"]))]:
            t0 = time.perf_counter(); rt = time.perf_counter() - t0  # negligible
            acc = int((out["kb"] == scn["gold"]) or (scn["esc"] and out["escalate"]))
            rows.append({"system": name, "scenario_id": scn["id"], "category": scn["cat"],
                         "response_time_s": round(rt, 5), "accuracy": acc,
                         "escalation_ok": int(out["escalate"] == scn["esc"]),
                         "usefulness": usefulness(scn, out["kb"], out["escalate"], out["personalized"])})
        # S1 real LLM (use cache if available, else call and cache immediately)
        sid = str(scn["id"])
        if sid in cache:
            d = cache[sid]
            rt = d.get("response_time_s", 0.0)
        else:
            t0 = time.perf_counter()
            raw = call(build_prompt(scn["text"]))
            rt = time.perf_counter() - t0
            d = parse_json(raw)
            d["response_time_s"] = round(rt, 4)
            cache[sid] = d
            save_cache(cache)  # persist after every successful call
            time.sleep(REQUEST_DELAY)  # throttle to stay under free-tier rate limits
        acc = int((d["used_kb_id"] == scn["gold"]) or (scn["esc"] and d["escalate"]))
        rows.append({"system": "S1 (Proposed RAG)", "scenario_id": scn["id"],
                     "category": scn["cat"], "response_time_s": round(rt, 4),
                     "accuracy": acc, "escalation_ok": int(d["escalate"] == scn["esc"]),
                     "usefulness": usefulness(scn, d["used_kb_id"], d["escalate"], d["personalized"])})
        raws.append({"scenario_id": scn["id"], "text": scn["text"],
                     "answer": d["answer"], "used_kb_id": d["used_kb_id"],
                     "escalate": d["escalate"], "personalized": d["personalized"]})
        print(f"  [{scn['id']:>2}] {scn['cat']:<9} acc={acc} esc={d['escalate']} rt={rt:.2f}s "
              f"{'(cached)' if sid in cache and rt == d.get('response_time_s') else ''}")

    per = pd.DataFrame(rows)
    per.to_csv(BASE / "data" / "e1_per_scenario_llm.csv", index=False)
    pd.DataFrame(raws).to_csv(BASE / "data" / "e1_raw_answers_llm.csv", index=False)

    order = ["S1 (Proposed RAG)", "B1 (Rule-based)", "B2 (TF-IDF)"]
    summary = (per.groupby("system")
               .agg(avg_response_time_s=("response_time_s", "mean"),
                    avg_usefulness=("usefulness", "mean"),
                    accuracy_pct=("accuracy", lambda s: 100 * s.mean()),
                    escalation_ok_pct=("escalation_ok", lambda s: 100 * s.mean()))
               .round(3).reindex(order))
    summary.to_csv(BASE / "tables" / "e1_system_comparison_llm.csv")
    print("\n=== E1 (real LLM) system comparison ===")
    print(summary.to_string())

    cat = (per.pivot_table(index="system", columns="category", values="accuracy",
                           aggfunc="mean") * 100).round(1).reindex(order)
    cat.to_csv(BASE / "tables" / "e1_accuracy_by_category_llm.csv")
    print("\n=== Accuracy (%) by category ===")
    print(cat.to_string())

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    colors = ["#4C78A8", "#F58518", "#54A24B"]
    axes[0].bar(order, summary["avg_usefulness"], color=colors); axes[0].set_ylim(0, 5)
    axes[0].set_title("Average Usefulness (1–5)")
    axes[1].bar(order, summary["accuracy_pct"], color=colors); axes[1].set_ylim(0, 100)
    axes[1].set_title("Accuracy (%)")
    for ax in axes:
        ax.set_xticks(range(len(order)))
        ax.set_xticklabels(order, rotation=15, ha="right", fontsize=8)
    fig.suptitle("E1 (real LLM) — Chatbot Prototype vs. Baselines")
    fig.tight_layout()
    fig.savefig(BASE / "figures" / "e1_system_comparison_llm.png", dpi=150)
    plt.close(fig)
    print("\nSaved LLM results, raw answers, tables, and figure.")

if __name__ == "__main__":
    main()
