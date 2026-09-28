"""
Q&A Module
----------
Answers general-knowledge and academic questions using Gemini 1.5 Pro.
"""

from gemini_client import get_model


def answer_question_with_gemini(question: str) -> str:
    try:
        model = get_model()
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"\u26a0 Error in QnA: {e}"
