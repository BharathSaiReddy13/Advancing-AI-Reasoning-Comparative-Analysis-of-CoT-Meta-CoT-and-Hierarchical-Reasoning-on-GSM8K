"""
Dataset utilities for ARC Challenge (ARC-easy).
"""

import json
from typing import List, Dict


def load_arc_dataset(path: str) -> List[Dict]:
    """
    Load ARC dataset from JSON file.

    Args:
        path (str): Path to ARC dataset file.

    Returns:
        List[Dict]: List of examples with question, choices, and answer.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = [json.loads(line) for line in f]
    return data
