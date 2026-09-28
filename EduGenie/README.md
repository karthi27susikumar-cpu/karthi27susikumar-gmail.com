# EduGenie — Google Gemini Powered Learning Assistant

A lightweight AI-powered educational assistant. Ask questions, get simplified
explanations, generate quizzes, summarize passages, and get personalized
learning paths.

## Features
- **Q&A** — general-knowledge and academic questions (Gemini 1.5 Pro)
- **Explanation** — simplified concept explanations (local LaMini-Flan-T5-783M)
- **Quiz generation** — 3 MCQs from any passage or topic (Gemini)
- **Summarization** — condense long passages (Gemini)
- **Learning paths** — beginner → advanced structured plan with resources (Gemini)

## Project structure
```
EduGenie/
├── main.py                 # FastAPI app & routes
├── gemini_client.py         # Shared Gemini configuration
├── explanation_module.py    # Local LaMini-Flan-T5 explanations
├── qna.py                   # Gemini-powered Q&A
├── quiz_module.py           # Gemini-powered quiz generation
├── summary_module.py        # Gemini-powered summarization
├── learning_path.py         # Gemini-powered learning paths
├── templates/index.html     # Frontend
├── static/style.css         # Styling
├── static/script.js         # Frontend logic
├── requirements.txt
└── .env.example
```

## Setup

1. **Install Python 3.10+** if you don't already have it.

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Note: `torch` + `transformers` download is sizeable and the first call to
   `/explain/` will also download the LaMini-Flan-T5-783M weights (~3 GB) the
   first time it runs.

4. **Get a Gemini API key** from [Google AI Studio](https://aistudio.google.com/):
   - Sign in with your Google account
   - Create a new project and enable the Gemini API
   - Generate an API key

5. **Configure your key:**
   ```bash
   cp .env.example .env
   # then edit .env and paste your key into GOOGLE_API_KEY=
   ```

## Run

```bash
uvicorn main:app --reload
```

Open **http://127.0.0.1:8000** in your browser.

## API reference

| Method | Endpoint | Body / Query | Purpose |
|---|---|---|---|
| GET | `/qa?question=...` | — | Ask a question |
| POST | `/explain/` | `{"topic": "..."}` | Get a simplified explanation |
| POST | `/summarize/` | `{"text": "..."}` | Summarize a passage |
| POST | `/quiz` | `{"text": "..."}` | Generate a 3-question MCQ quiz |
| GET | `/learn/recommendations?topic=...` | — | Get a structured learning path |

## Notes
- Without a valid `GOOGLE_API_KEY`, the Gemini-backed endpoints (`/qa`,
  `/summarize/`, `/quiz`, `/learn/recommendations`) will return an error
  message rather than crash.
- The explanation endpoint runs entirely locally and needs no API key, but
  is CPU/RAM heavier on first load.
