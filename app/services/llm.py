from openai import OpenAI
from app.core.config import settings

SYSTEM_PROMPT = """You are a document question-answering assistant.
Answer using the supplied document context. Do not invent facts.
If the context does not contain the answer, clearly say that the answer was
not found in the provided documents. You may use the conversation history
only to understand references in the user's question; factual claims must
still be grounded in the supplied document context. Cite sources using
[Source N] notation."""

def generate_answer(question: str, contexts: list[dict], history=None) -> str:
    if not contexts:
        return "I could not find relevant information in the indexed documents."

    context = "\n\n".join(
        f"[Source {i}] {c['document']} — page {c['page']}\n{c['text']}"
        for i, c in enumerate(contexts, 1)
    )

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for item in (history or [])[-10:]:
        if item["role"] in {"user", "assistant"}:
            messages.append({"role": item["role"], "content": item["content"]})

    messages.append({
        "role": "user",
        "content": f"Document context:\n{context}\n\nQuestion: {question}",
    })

    client = OpenAI(
        base_url=settings.llm_base_url,
        api_key=settings.llm_api_key,
    )
    response = client.chat.completions.create(
        model=settings.llm_model,
        temperature=0.1,
        messages=messages,
    )
    return response.choices[0].message.content or "No answer was generated."
