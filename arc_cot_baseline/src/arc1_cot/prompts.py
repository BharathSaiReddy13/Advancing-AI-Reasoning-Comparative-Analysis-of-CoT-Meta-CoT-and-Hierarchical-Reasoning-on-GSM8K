"""
Prompt templates for Chain-of-Thought reasoning.
"""

from typing import List


def build_cot_prompt(question: str, choices: List[str]) -> str:
    """
    Construct a CoT-style prompt for GPT-2.

    Args:
        question (str): The input question.
        choices (List[str]): Multiple choice options.

    Returns:
        str: A formatted CoT prompt string.
    """
    formatted_choices = "\n".join(
        [f"{chr(65+i)}. {choice}" for i, choice in enumerate(choices)]
    )
    return (
        f"Question: {question}\n\n"
        f"Choices:\n{formatted_choices}\n\n"
        "Let's think step by step:\n"
    )
