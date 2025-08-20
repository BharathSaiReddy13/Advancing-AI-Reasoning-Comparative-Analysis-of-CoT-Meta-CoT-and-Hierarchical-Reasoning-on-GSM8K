#!/usr/bin/env bash
set -euo pipefail

# Usage: bash scripts/run_cot_arc1.sh [split] [limit] [model_name]
# Example: bash scripts/run_cot_arc1.sh validation 10 gpt2

SPLIT="${1:-validation}"   # validation or test
LIMIT="${2:-10}"           # number of samples (int) or "null" for all
MODEL="${3:-gpt2}"         # e.g., gpt2, gpt2-medium

# Ensure we can import the package from src/
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.."; pwd)"
export PYTHONPATH="${REPO_ROOT}/src:${PYTHONPATH}"

echo "[INFO] Running CoT baseline on ARC-1 | split=${SPLIT} | limit=${LIMIT} | model=${MODEL}"

python - <<'PY'
import os
import sys
from datasets import load_dataset
from arc1_cot.evaluate import evaluate

# Read settings passed from bash
split = os.environ.get("SPLIT", "validation")
limit = os.environ.get("LIMIT", "10")
model_name = os.environ.get("MODEL", "gpt2")

# Convert limit to int or None
if isinstance(limit, str) and limit.lower() == "null":
    limit = None
else:
    limit = int(limit)

# Load ARC Challenge split via HF datasets
print(f"[INFO] Loading ai2_arc: ARC-Challenge ({split}) …")
hf_ds = load_dataset("ai2_arc", "ARC-Challenge", split=split)

# Transform to our expected schema: {question, choices: [A..], answer: 'A'..'E'}
def to_example(ex):
    labels = ex["choices"]["label"]   # ['A','B',...]
    texts  = ex["choices"]["text"]    # ['optA','optB',...]
    pairs = sorted(zip(labels, texts), key=lambda x: x[0])  # sort by label
    choices = [t for _, t in pairs]
    return {
        "question": ex["question"],
        "choices": choices,
        "answer": ex["answerKey"]
    }

examples = [to_example(ex) for ex in hf_ds]
if limit is not None:
    examples = examples[:limit]
print(f"[INFO] Prepared {len(examples)} examples.")

# Evaluate
acc = evaluate(examples, model_name=model_name)
print(f"[RESULT] Accuracy: {acc:.4f}")
PY
