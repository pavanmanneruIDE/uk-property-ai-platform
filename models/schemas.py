from pydantic import BaseModel
from typing import List

class Doc(BaseModel):
    source: str
    text: str

class IngestRequest(BaseModel):
    docs: List[Doc]

class QueryRequest(BaseModel):
    question: str
    top_k: int = 5
