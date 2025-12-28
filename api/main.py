from fastapi import FastAPI
from pydantic import BaseModel
from rag.pipeline import query_rag

app = FastAPI(title="UK Property AI Platform")

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query")
def query(req: QueryRequest):
    answer = query_rag(req.question)
    return {"answer": answer}
