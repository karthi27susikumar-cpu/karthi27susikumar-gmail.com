"""
Explanation Module
-------------------
Uses a lightweight, locally-run instruction-tuned model (LaMini-Flan-T5-783M)
to turn a topic name into a simple, student-friendly explanation.

Running fully locally means this module works even without an internet
connection or a Gemini API key, at the cost of somewhat less polished
output than the cloud-backed modules.
"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "MBZUAI/LaMini-Flan-T5-783M"

# Loaded lazily so the app can start quickly and only pay the (one-time)
# download / load cost the first time an explanation is actually requested.
_explain_tokenizer = None
_explain_model = None


def _load_model():
    global _explain_tokenizer, _explain_model
    if _explain_model is None:
        _explain_tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        _explain_model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return _explain_tokenizer, _explain_model


def explain_topic(topic: str) -> str:
    """Generate a simple, clear explanation of `topic` for a school student."""
    tokenizer, model = _load_model()

    input_text = (
        f"Explain the concept of '{topic}' in a simple and clear way "
        f"for a school student."
    )
    inputs = tokenizer(input_text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            do_sample=True,
        )

    explanation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return explanation
