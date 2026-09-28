"""
Learning Path Module
---------------------
Builds a structured, adaptive learning path (beginner -> advanced) for a
given topic, complete with suggested resources.
"""

import traceback

from gemini_client import get_model


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured and adaptive learning path including key topics, order of learning, and resources (videos, articles, or books).
Include beginner, intermediate, and advanced levels if needed.
"""
    try:
        model = get_model()
        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text
        elif hasattr(response, "parts") and response.parts:
            return response.parts[0].text
        else:
            return "\u274c Could not extract content from Gemini response."
    except Exception as e:
        traceback.print_exc()
        return f"\u274c Error occurred: {str(e)}"
