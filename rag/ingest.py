import hashlib

def chunk_text(text: str, size: int = 1000, overlap: int = 150):
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap
        if start < 0:
            start = 0
    return chunks

def make_chunk_id(source: str, idx: int):
    raw = f"{source}-{idx}".encode()
    return hashlib.sha1(raw).hexdigest()
