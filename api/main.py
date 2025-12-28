from fastapi import FastAPI
from models.schemas import IngestRequest, QueryRequest
from rag.ingest import chunk_text, make_chunk_id
from rag.embeddings import embed_texts
from rag.vector_store import Chunk, FaissVectorStore
from rag.pipeline import answer_question

app = FastAPI(title="UK Property AI Platform")

store = FaissVectorStore(dim=768)

@app.get("/health")
def health():
    return {"chunks": len(store.chunks)}

@app.post("/ingest/docs")
def ingest(req: IngestRequest):
    texts, chunks = [], []

    for doc in req.docs:
        for i, ch in enumerate(chunk_text(doc.text)):
            cid = make_chunk_id(doc.source, i)
            chunks.append(Chunk(cid, ch, {"source": doc.source}))
            texts.append(ch)

    vectors = embed_texts(texts)
    store.add(vectors, chunks)
    return {"ingested_chunks": len(chunks)}

@app.post("/query")
def query(req: QueryRequest):
    return answer_question(store, req.question, req.top_k)
