"""
Small shared helper so every module configures the Gemini API the same way,
using a key loaded from the environment (see .env.example).
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

GEMINI_MODEL_NAME = "models/gemini-1.5-pro"


def get_model():
    if not API_KEY:
        raise RuntimeError(
            "GOOGLE_API_KEY is not set. Copy .env.example to .env and add your "
            "Gemini API key from https://aistudio.google.com/"
        )
    return genai.GenerativeModel(model_name=GEMINI_MODEL_NAME)
