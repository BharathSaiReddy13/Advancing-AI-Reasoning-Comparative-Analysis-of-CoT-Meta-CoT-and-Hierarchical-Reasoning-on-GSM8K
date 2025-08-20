# tests/test_prompts.py
import os
import sys

# Ensure src/ is importable when running pytest from repo root
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from arc1_cot.prompts import build_cot_prompt


def test_build_cot_prompt_includes_structure():
    q = "Which of the following is a mammal?"
    choices = ["Shark", "Frog", "Dolphin", "Eagle"]
    prompt = build_cot_prompt(q, choices)

    # Basic structure checks
    assert "Question:" in prompt
    assert "Choices:" in prompt
    assert "Let's think step by step:" in prompt

    # Choices labeled A., B., …
    assert "A. Shark" in prompt
    assert "B. Frog" in prompt
    assert "C. Dolphin" in prompt
    assert "D. Eagle" in prompt
