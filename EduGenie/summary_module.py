"""
Summary Module
--------------
Summarizes long educational passages into short, easy-to-read versions
using Gemini's generative capabilities.
"""

from gemini_client import get_model


def summarize_text(text: str) -> str:
    try:
        model = get_model()
        prompt = f"Summarize the following text in simple language:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"\u26a0 Error in Summary: {e}"
