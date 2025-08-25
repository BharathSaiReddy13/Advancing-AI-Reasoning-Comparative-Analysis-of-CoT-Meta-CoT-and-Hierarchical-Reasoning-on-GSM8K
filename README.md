# Advancing AI Reasoning: Comparative Analysis of CoT, Meta-CoT, and Hierarchical Reasoning on ARC 1

> **Work in Progress**
> Maintainer: *\[Bharath Sai Reddy]*

---

## Project Overview

This project aims to systematically compare three state-of-the-art reasoning strategies for large language models on the **ARC 1** benchmark:

* **Chain-of-Thought (CoT) Prompting**: Standard prompting with and without self-consistency.
* **Meta-CoT (Stanford)**: Meta-reasoning with multiple reasoning paths and meta-prompting strategies \[2].
* **Hierarchical Reasoning Model (Sapient Intelligence)**: A recurrent, two-level reasoning model inspired by human cognition \[3].

**Key Evaluation Dimensions:**

* Exact-match accuracy
* Reasoning trace quality (faithfulness, clarity)
* Generalization across problem types
* Efficiency (tokens, latency, sample complexity)

---

##  Motivation

While **CoT prompting** has shown remarkable improvements in LLM reasoning \[1], challenges remain in **uncertainty handling** and **multi-step logical inference**.

Recent advances:

* **Meta-CoT** \[2] leverages meta-prompting and diverse reasoning paths to enhance robustness.
* **HRM** \[3] introduces a hierarchical architecture, reflecting aspects of **human cognitive reasoning**.

A **side-by-side benchmark** of these paradigms provides deeper insight into their comparative strengths, weaknesses, and potential for future reasoning systems.

---

##  Project Status

* [x] Initial literature review and planning
* [ ] CoT baseline implementation
* [ ] Meta-CoT integration (in progress)
* [ ] HRM pipeline setup
* [ ] GSM8K experiments and analysis

---

## Getting Started

1. **Clone this repo** (currently private development).

   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```
2. **Install requirements**:

   ```bash
   pip install -r requirements.txt
   ```
3. **Download GSM8K** (via HuggingFace Datasets or original repo).

   ```python
   from datasets import load_dataset
   ds = load_dataset("gsm8k", "main")
   ```
4. **Run Baseline (coming soon):**

   ```bash
   python scripts/run_cot_baseline.py
   ```
5. **Additional frameworks** (Meta-CoT, HRM) will be added as development progresses.

---

## Roadmap

* [ ] Finish baseline CoT runs and document results
* [ ] Reproduce and test **Meta-CoT** following Stanford’s implementation \[2]
* [ ] Integrate **HRM** as described in Sapient’s research \[3]
* [ ] Comprehensive benchmark (accuracy, reasoning trace quality, cost)
* [ ] Compose short paper and submit to workshop/conference

---

## 📚 References

* \[1] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou. *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. arXiv:2201.11903 (2022).
* \[2] Violet Xiang, Charlie Snell, Kanishk Gandhi, Alon Albalak, Anikait Singh, Chase Blagden, Duy Phung, Rafael Rafailov, Nathan Lile, Dakota Mahan, Louis Castricato, Jan-Philipp Franken, Nick Haber, Chelsea Finn. *Towards System 2 Reasoning in LLMs: Learning How to Think With Meta Chain-of-Thought*. arXiv:2501.04682 (2025).
* \[3] Guan Wang, Jin Li, Yuhao Sun, Xing Chen, Changling Liu, Yue Wu, Meng Lu, Sen Song, Yasin Abbasi Yadkori. *Hierarchical Reasoning Model*. arXiv:2506.21734 (2025).

---

## Contact

Maintainer: \[Bharath Sai Reddy]
Email: \[bharathsaireddy7161@gmail.com]

---
arc1-cot-baseline/
├─ README.md
├─ LICENSE
├─ requirements.txt
├─ pyproject.toml
├─ .gitignore
├─ configs/
│  ├─ default.yaml
│  └─ eval_arc1.yaml
├─ src/
│  └─ arc1_cot/
│     ├─ __init__.py
│     ├─ utils.py
│     ├─ dataset.py
│     ├─ prompts.py
│     ├─ model_gpt2.py
│     ├─ cot_infer.py
│     ├─ parsing.py
│     └─ evaluate.py
├─ scripts/
│  └─ run_cot_arc1.sh
├─ tests/
│  ├─ test_prompts.py
│  ├─ test_parsing.py
│  └─ test_infer_smoke.py
├─ outputs/            # (gitignored)
└─ data/               # (gitignored)
