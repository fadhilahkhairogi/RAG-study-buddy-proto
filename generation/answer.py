from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def answer(query, contexts):
    context_text = "\n\n".join(contexts)

    prompt = f"""
Answer ONLY using the context.
If not stated, say "Not stated in the papers."

Context:
{context_text}

Question:
{query}
"""

    return client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        # temperature=0
    ).choices[0].message.content
