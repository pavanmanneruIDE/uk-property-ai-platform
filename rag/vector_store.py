import faiss
import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Any, Tuple

@dataclass
class Chunk:
    id: str
    text: str
    metadata: Dict[str, Any]

class FaissVectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatIP(dim)
        self.chunks: List[Chunk] = []

    def add(self, vectors: np.ndarray, chunks: List[Chunk]):
        faiss.normalize_L2(vectors)
        self.index.add(vectors)
        self.chunks.extend(chunks)

    def search(self, query_vec: np.ndarray, top_k: int):
        query_vec = query_vec.reshape(1, -1)
        faiss.normalize_L2(query_vec)
        scores, idxs = self.index.search(query_vec, top_k)

        results = []
        for i, score in zip(idxs[0], scores[0]):
            if i == -1:
                continue
            results.append((self.chunks[i], float(score)))
        return results
