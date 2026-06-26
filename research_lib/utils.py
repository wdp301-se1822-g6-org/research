import os
import json
import time
import re
from pathlib import Path

def load_env_file():
    """Locate and load variables from a .env file into os.environ."""
    curr = Path(__file__).resolve()
    for _ in range(4):
        env_path = curr.parent / ".env"
        if env_path.exists():
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        k, v = line.split("=", 1)
                        os.environ[k.strip()] = v.strip().strip("'\"")
            break
        curr = curr.parent

def load_scenarios(base_dir=None):
    """Load scenarios.json from baseline or base directory."""
    if base_dir is None:
        # Default fallback to find scenarios.json relative to research_lib or root
        base_dir = Path(__file__).resolve().parents[1]
    
    scenarios_path = Path(base_dir) / "06_experiment_results" / "scenarios.json"
    if not scenarios_path.exists():
        scenarios_path = Path(base_dir) / "scenarios.json"
        
    with open(scenarios_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_kb():
    """Returns the default Knowledge Base dictionary."""
    return {
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

def with_retry(fn, retries=6):
    """Decorator to call fn(prompt) with exponential backoff on rate-limit / transient errors."""
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

def make_llm_caller(provider=None, model=None):
    """Factory to create an LLM caller based on provider configuration."""
    load_env_file()
    provider = (provider or os.environ.get("LLM_PROVIDER", "gemini")).lower()
    
    if provider == "gemini":
        import google.generativeai as genai
        raw = os.environ.get("GEMINI_API_KEYS") or os.environ.get("GEMINI_API_KEY", "")
        keys = [k.strip() for k in re.split(r"[,\s]+", raw) if k.strip()]
        if not keys:
            raise ValueError("No Gemini key found (set GEMINI_API_KEYS or GEMINI_API_KEY).")
        mdl = model or os.environ.get("LLM_MODEL", "gemini-2.5-flash-lite")
        print(f"  ({len(keys)} Gemini key(s) loaded for rotation)")
        state = {"i": 0, "exhausted": set()}
        
        def call(prompt):
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
            state["exhausted"].clear()
            raise RuntimeError("All Gemini keys hit quota (429)")
        return call
        
    elif provider == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", ""))
        mdl = model or os.environ.get("LLM_MODEL", "gpt-4o-mini")
        def call(prompt):
            r = client.chat.completions.create(
                model=mdl, temperature=0.2,
                messages=[{"role": "user", "content": prompt}])
            return r.choices[0].message.content
        return call
        
    elif provider == "anthropic":
        import anthropic
        client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))
        mdl = model or os.environ.get("LLM_MODEL", "claude-haiku-4-5-20251001")
        def call(prompt):
            r = client.messages.create(
                model=mdl, max_tokens=400, temperature=0.2,
                messages=[{"role": "user", "content": prompt}])
            return r.content[0].text
        return call
        
    raise ValueError(f"Unknown LLM_PROVIDER={provider}")

def parse_json_response(raw, kb=None):
    """Parse strict JSON output from LLM response helper."""
    if kb is None:
        kb = load_kb()
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    if not m:
        return {"answer": raw.strip(), "used_kb_id": None, "escalate": False, "personalized": False}
    try:
        d = json.loads(m.group(0))
    except Exception:
        return {"answer": raw.strip(), "used_kb_id": None, "escalate": False, "personalized": False}
    kid = d.get("used_kb_id")
    if kid not in kb:
        kid = None
    return {"answer": d.get("answer", ""), "used_kb_id": kid,
            "escalate": bool(d.get("escalate", False)),
            "personalized": bool(d.get("personalized", False))}
