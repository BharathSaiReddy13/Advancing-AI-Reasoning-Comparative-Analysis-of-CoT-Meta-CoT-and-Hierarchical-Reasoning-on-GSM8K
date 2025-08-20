# tests/test_parsing.py
import os
import sys

# Ensure src/ is importable when running pytest from repo root
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from arc1_cot.parsing import extract_final_answer


def test_parsing_simple_answer_colon():
    out = "Reasoning...\nAnswer: C"
    assert extract_final_answer(out) == "C"


def test_parsing_case_insensitive():
    out = "final steps... answer c"
    assert extract_final_answer(out) == "C"


def test_parsing_no_answer_returns_none():
    out = "Model rambled without concluding."
    assert extract_final_answer(out) is None
