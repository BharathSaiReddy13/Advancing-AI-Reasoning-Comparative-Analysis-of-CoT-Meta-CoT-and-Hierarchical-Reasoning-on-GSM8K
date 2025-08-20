"""
Wrapper for GPT-2 small model (Hugging Face Transformers).
"""

from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch


class GPT2Wrapper:
    """A thin wrapper around GPT-2 for text generation."""

    def __init__(self, model_name: str = "gpt2", device: str = None):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate(self, prompt: str, max_new_tokens: int = 100) -> str:
        """Generate text given a prompt."""
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
