"""
Quiz Module
-----------
Generates 3 multiple-choice questions (4 options each) from a passage or
topic, using Gemini to produce structured JSON output.
"""

import json
import re

from gemini_client import get_model


def clean_json_block(text: str) -> str:
    """Strip Markdown ```json ... ``` fences if the model added them."""
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()


def generate_quiz(text: str) -> list:
    try:
        model = get_model()

        prompt = f"""
You are a quiz generator.

From the following passage, create 3 multiple-choice questions. Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON**, like this:
[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{text}
"""
        response = model.generate_content(prompt)
        quiz_text = response.text.strip()

        cleaned_text = clean_json_block(quiz_text)
        quiz = json.loads(cleaned_text)
        return quiz
    except Exception as e:
        return [{"error": f"\u26a0 Error generating quiz: {e}"}]
