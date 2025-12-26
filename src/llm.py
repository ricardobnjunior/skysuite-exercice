import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def build_prompt(question: str, passages: list[dict]) -> str:
    """Build a prompt with retrieved context for the LLM."""
    context = "\n".join([f"- {p['text']}" for p in passages])

    return f"""Based on the following context, answer the question.
If the answer cannot be found in the context, say so.

Context:
{context}

Question: {question}

Answer:"""


def ask(question: str, passages: list[dict], model: str = "openai/gpt-4o-mini") -> str:
    """Send question with context to LLM and return the answer."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not set in .env")

    prompt = build_prompt(question, passages)

    response = requests.post(
        OPENROUTER_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 512
        },
        timeout=30
    )
    response.raise_for_status()

    data = response.json()
    if "error" in data:
        raise RuntimeError(f"API error: {data['error']}")

    return data["choices"][0]["message"]["content"].strip()
