import time
import os
import ollama
from dotenv import load_dotenv
from rag.embeddings import embed_query
from rag.vector_store import Chunk, FaissVectorStore

load_dotenv()
LLM_MODEL = os.getenv("LLM_MODEL", "llama3.2")

def build_prompt(question, retrieved):
    context = "\n\n".join(
        f"[{i+1}] {chunk.text}"
        for i, (chunk, _) in enumerate(retrieved)
    )

    return f"""
Use only the context below to answer.

Context:
{context}

Question:
{question}

Answer with citations like [1], [2].
"""

def answer_question(store: FaissVectorStore, question: str, top_k: int):
    start = time.time()
    qvec = embed_query(question)
    retrieved = store.search(qvec, top_k)

    prompt = build_prompt(question, retrieved)

    resp = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.2}
    )

    return {
        "answer": resp["message"]["content"],
        "citations": [
            {"id": i+1, "score": score}
            for i, (_, score) in enumerate(retrieved)
        ],
        "latency_ms": int((time.time() - start) * 1000)
    }
