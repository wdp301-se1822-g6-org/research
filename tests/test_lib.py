import pytest
from research_lib import load_kb, parse_json_response

def test_load_kb():
    kb = load_kb()
    assert isinstance(kb, dict)
    assert "kb_hours" in kb
    assert "kw" in kb["kb_hours"]

def test_parse_json_response():
    raw_json = '{"answer": "Xin chào", "used_kb_id": "kb_hours", "escalate": false, "personalized": true}'
    res = parse_json_response(raw_json)
    assert res["answer"] == "Xin chào"
    assert res["used_kb_id"] == "kb_hours"
    assert res["escalate"] is False
    assert res["personalized"] is True
