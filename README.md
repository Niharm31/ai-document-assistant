# AI Document Assistant

> **Local-first RAG for intelligent PDF question answering**

Upload PDFs, retrieve relevant context, and ask questions with grounded answers and source references.

<img src="https://img.shields.io/badge/Python-3.11%2B-3776AB" alt="Python">
<img src="https://img.shields.io/badge/FastAPI-009688" alt="FastAPI">
<img src="https://img.shields.io/badge/FAISS-7C3AED" alt="FAISS">
<img src="https://img.shields.io/badge/Docker-2496ED" alt="Docker">
<img src="https://img.shields.io/badge/License-MIT-22C55E" alt="MIT">

---

## Overview

AI Document Assistant is a **Retrieval-Augmented Generation (RAG)** application for querying PDF documents with a local or OpenAI-compatible LLM.

Instead of sending an entire document to the model, the system retrieves the most relevant content first and uses it as context for the answer.

## Core Pipeline

```text
PDF
  ↓
PyMuPDF
  ↓
Page-aware Chunking
  ↓
Sentence Transformers
  ↓
FAISS
  ↓
Semantic Retrieval
  ↓
Relevant Context
  ↓
LLM
  ↓
Answer + Sources
```

## Features

| | Feature |
|---|---|
| 📄 | PDF upload and text extraction |
| 🔎 | Semantic document search |
| 🧠 | Retrieval-Augmented Generation |
| 📚 | Multi-document querying |
| 💬 | Conversation history |
| 📍 | Source-page references |
| 🦙 | Local Qwen3 + llama.cpp |
| 🚀 | FastAPI REST API |
| 🐳 | Docker deployment |
| 🧪 | Automated testing and RAG evaluation |
| ⚙️ | GitHub Actions CI |

## Architecture

```text
                     ┌─────────────────┐
                     │     Browser     │
                     │  Web Interface  │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │     FastAPI     │
                     │     Backend     │
                     └────────┬────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
          ┌─────────────┐           ┌─────────────┐
          │ PDF Pipeline│           │   Retrieval  │
          │   PyMuPDF   │           │    FAISS     │
          └──────┬──────┘           └──────┬──────┘
                 │                         │
                 └────────────┬────────────┘
                              ▼
                     ┌─────────────────┐
                     │      Qwen3      │
                     │    llama.cpp    │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ Answer + Sources│
                     └─────────────────┘
```

## Tech Stack

**Backend**

`Python` · `FastAPI` · `Pydantic` · `SQLAlchemy`

**AI / Retrieval**

`Sentence Transformers` · `FAISS` · `RAG` · `Qwen3` · `llama.cpp`

**Frontend**

`HTML` · `CSS` · `JavaScript`

**Infrastructure**

`Docker` · `Docker Compose` · `GitHub Actions`

## Quick Start

### Requirements

- Python 3.11+
- Git
- OpenAI-compatible LLM endpoint

For local inference:

- llama.cpp
- Compatible GGUF model

### Clone

```bash
git clone https://github.com/Niharm31/ai-document-assistant.git
cd ai-document-assistant
```

### Install

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Configure

Create `.env` from `.env.example`.

For local llama.cpp:

```env
LLM_BASE_URL=http://127.0.0.1:8080/v1
LLM_API_KEY=local
LLM_MODEL=your-model-path
```

### Run

```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open:

```text
http://127.0.0.1:8000
```

## Local LLM

The application supports Qwen3 GGUF models through llama.cpp.

```text
Browser
   │
   ▼
FastAPI :8000
   │
   ▼
llama.cpp :8080
   │
   ▼
Qwen3
```

Check llama.cpp:

```powershell
curl http://127.0.0.1:8080/health
```

Expected:

```json
{"status":"ok"}
```

## Docker

```bash
docker compose up --build
```

When llama.cpp runs directly on Windows while the application runs inside Docker:

```env
LLM_BASE_URL=http://host.docker.internal:8080/v1
```

See [`DEPLOYMENT.md`](DEPLOYMENT.md) for deployment details.

## API

| Endpoint | Method | Purpose |
|---|---|---|
| `/health` | GET | Health check |
| `/ready` | GET | Readiness check |
| `/api/documents` | GET | List documents |
| `/api/documents/upload` | POST | Upload PDF |
| `/api/documents/{id}` | DELETE | Delete document |
| `/api/chat` | POST | Ask a question |
| `/api/chat/{session_id}/history` | GET | Conversation history |

## Evaluation

Retrieval evaluation includes:

- **Hit@K**
- **Mean Reciprocal Rank (MRR)**

Run:

```bash
python scripts/evaluate_rag.py
```

## Testing

```bash
pytest
```

## Project Structure

```text
ai-document-assistant/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   └── services/
│
├── frontend/
├── tests/
├── evals/
├── scripts/
├── docs/
├── data/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── DEPLOYMENT.md
└── README.md
```

## Roadmap

- [ ] Streaming responses
- [ ] OCR for scanned PDFs
- [ ] Hybrid search
- [ ] Reranking
- [ ] Authentication
- [ ] Cloud deployment
- [ ] Distributed vector storage

## License

MIT License

## Author

**Nihar Mandal**

BTech — Artificial Intelligence & Machine Learning

[GitHub](https://github.com/Niharm31) · [LinkedIn](https://www.linkedin.com/in/nihar-mandal-b512b5288)
