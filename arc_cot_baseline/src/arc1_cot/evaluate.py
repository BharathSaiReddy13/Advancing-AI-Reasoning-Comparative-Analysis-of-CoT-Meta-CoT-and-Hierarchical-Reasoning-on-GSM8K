"""
Evaluation loop for ARC-CoT baseline.
"""

from typing import List, Dict
from .cot_infer import COTInference
from .parsing import extract_final_answer


def evaluate(dataset: List[Dict], model_name: str = "gpt2") -> float:
    """
    Evaluate CoT inference baseline on dataset.

    Args:
        dataset (List[Dict]): List of examples with "question", "choices", "answer".
        model_name (str): GPT-2 variant.

    Returns:
        float: Accuracy score.
    """
    cot_runner = COTInference(model_name)
    correct = 0

    for example in dataset:
        output = cot_runner.run(example)
        pred = extract_final_answer(output)
        if pred == example["answer"]:
            correct += 1

    return correct / len(dataset)
