from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = "gpt-5-mini"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def answer(query, contexts, model=model):
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
        model=model,
        messages=[{"role": "user", "content": prompt}],
        # temperature=0
    ).choices[0].message.content

def answer_flexibly(query, contexts, model=model):
 
    context_text = "\n\n".join(contexts)

    prompt = f"""
Answer using the context as much as possible.
If the context is insufficient, make a reasoned answer but clearly higlight the parts that are your uncertain to INDICATE UNCERTAINTY.

Context:
{context_text}

Question:
{query}
"""
    return client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    ).choices[0].message.content