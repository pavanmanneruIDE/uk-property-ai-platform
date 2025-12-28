from typing import List
import numpy as np
import os
import ollama
from dotenv import load_dotenv

load_dotenv()

EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")

def embed_texts(texts: List[str]) -> np.ndarray:
    vectors = []
    for t in texts:
        resp = ollama.embeddings(
            model=EMBED_MODEL,
            prompt=t
        )
        vectors.append(resp["embedding"])
    return np.array(vectors, dtype=np.float32)

def embed_query(text: str) -> np.ndarray:
    return embed_texts([text])[0]
