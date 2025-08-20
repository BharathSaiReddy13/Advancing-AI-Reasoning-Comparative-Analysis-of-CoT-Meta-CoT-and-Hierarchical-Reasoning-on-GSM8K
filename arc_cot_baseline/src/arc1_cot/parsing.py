"""
Parse model outputs to extract final answers.
"""

import re
from typing import Optional


def extract_final_answer(output: str) -> Optional[str]:
    """
    Extract the final choice (A/B/C/...) from model output.

    Args:
        output (str): Generated CoT text.

    Returns:
        Optional[str]: Extracted choice or None.
    """
    match = re.search(r"Answer\s*[:\-]?\s*([A-D])", output, re.IGNORECASE)
    return match.group(1).upper() if match else None
