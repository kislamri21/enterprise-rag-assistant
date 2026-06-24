from ollama import chat
from app.vector_store import search_documents


def build_prompt(question: str, context_docs: list[str]) -> str:
    context = "\n\n".join(context_docs)

    return f"""
You are an enterprise AI assistant.

Answer the user's question using ONLY the provided context.
If the answer is not found, say:
"I could not find this information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""


def answer_question(question: str) -> str:
    context_docs = search_documents(question)
    prompt = build_prompt(question, context_docs)

    response = chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]
