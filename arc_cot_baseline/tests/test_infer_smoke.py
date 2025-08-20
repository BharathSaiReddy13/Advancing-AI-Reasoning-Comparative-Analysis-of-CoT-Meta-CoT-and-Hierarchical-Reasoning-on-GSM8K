# tests/test_infer_smoke.py
import os
import sys

# Ensure src/ is importable when running pytest from repo root
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from arc1_cot.evaluate import evaluate
from arc1_cot.model_gpt2 import GPT2Wrapper


def test_infer_smoke_monkeypatch(monkeypatch):
    """
    Smoke test: monkeypatch the GPT-2 generator to avoid downloading models.
    Ensures the pipeline (prompt -> generate -> parse -> evaluate) is wired correctly.
    """

    def fake_generate(self, prompt: str, max_new_tokens: int = 120) -> str:
        # Always output a valid answer line so parser succeeds
        return prompt + "\nAnswer: A"

    monkeypatch.setattr(GPT2Wrapper, "generate", fake_generate, raising=True)

    # Minimal synthetic dataset: one example with correct 'A'
    dataset = [
        {
            "question": "Which option is the first letter of the alphabet?",
            "choices": ["A", "B", "C", "D"],
            "answer": "A",
        }
    ]

    acc = evaluate(dataset, model_name="gpt2")
    assert acc == 1.0
