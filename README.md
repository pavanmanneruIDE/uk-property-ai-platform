# UK Property AI Platform

A production-style AI platform for natural-language querying over UK property transaction and regulatory data. This system leverages **Retrieval-Augmented Generation (RAG)** to provide grounded, explainable answers entirely on local CPU infrastructure.

---

## 🚀 Overview

This project implements a local RAG system that allows users to ask natural-language questions over UK property datasets. The system retrieves relevant context from ingested documents and uses a locally hosted language model to generate grounded, explainable answers with citations.

The project focuses on **system design, reliability, and data/AI integration** using production-style patterns rather than model training.

---

## 🏗️ Architecture

The system follows a standard RAG pipeline optimized for local performance:



**Data Flow:**
`Documents` ➔ `Chunking` ➔ `Local Embeddings` ➔ `Vector Index (FAISS)` ➔ `Retrieval` ➔ `Prompt Construction` ➔ `Local LLM Inference` ➔ `Answer with Citations`

### Core Components
* **FastAPI Service Layer:** Handles API routing and request validation.
* **Local Embedding Generation:** Converts text to vectors using `nomic-embed-text`.
* **Vector-Based Retrieval:** Semantic search via FAISS.
* **Local Language Model:** Powered by Ollama (`llama3.2`).
* **Schema-driven APIs:** Built with Pydantic for robust data validation.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Backend & API** | Python, FastAPI, Pydantic |
| **AI & Retrieval** | RAG, FAISS (vector search) |
| **Local AI Runtime** | Ollama |
| **Models** | `llama3.2` (LLM), `nomic-embed-text` (Embeddings) |
| **Environment** | Windows, CPU-only (no GPU required) |

---

## 📂 Project Structure

```text
uk-property-ai-platform/
├── api/
│   └── main.py          # FastAPI routes and server logic
├── rag/
│   ├── vector_store.py  # FAISS index management
│   ├── embeddings.py    # Local embedding generation
│   ├── ingest.py        # Document processing and chunking
│   └── pipeline.py      # RAG coordination logic
├── models/
│   └── schemas.py       # Pydantic request/response models
├── requirements.txt     # Python dependencies
├── .env                 # Environment configuration
└── README.md            # Project documentation

```

---

## ⚙️ Running Locally

### Prerequisites

* **Python 3.10+**
* **Ollama** installed on Windows.

### Step 1: Start Ollama

Ensure the Ollama server is running and pull the necessary models:

```powershell
# In your terminal
ollama serve

# In a separate window
ollama pull llama3.2
ollama pull nomic-embed-text

```

### Step 2: Environment Setup

```powershell
# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

```

### Step 3: Configuration

Create a `.env` file in the repository root:

```env
LLM_MODEL=llama3.2
EMBED_MODEL=nomic-embed-text

```

### Step 4: Run the API

```powershell
uvicorn api.main:app --reload

```

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Health Endpoint:** [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

---

## 💡 Usage

### Ingesting Documents

Documents are chunked and indexed into FAISS via the `/ingest/docs` endpoint.

```json
{
  "docs": [
    {
      "source": "UK EPC guidance",
      "text": "Energy Performance Certificates in the UK rate properties from A to G."
    }
  ]
}

```

### Querying the System

Submit questions via the `/query` endpoint to receive grounded answers.

```json
{
  "question": "What does an EPC rating represent?",
  "top_k": 5
}

```

---

## ⚖️ Design Decisions

* **Why RAG?** Unlike fine-tuning, RAG supports frequently changing data, provides source-grounded answers to reduce "hallucinations," and lowers operational risk.
* **Why Local Models?** Provides full control over inference, eliminates external API costs/latencies, and ensures data privacy.
* **CPU Optimization:** Designed to be accessible on standard hardware without requiring high-end GPUs.

---

## 🛣️ Planned Enhancements

* [ ] Persist FAISS index to disk for long-term storage.
* [ ] Hybrid queries combining SQL (structured data) and RAG (unstructured text).
* [ ] Implementation of query caching and rate limiting.
* [ ] Support for additional UK property datasets (Land Registry, etc.).
