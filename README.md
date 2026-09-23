\# AI Document Assistant



> \*\*Local-first RAG for intelligent PDF question answering.\*\*



Upload PDFs, retrieve relevant context, and ask questions with grounded answers and source references.



!\[Python](https://img.shields.io/badge/Python-3.11%2B-3776AB)

!\[FastAPI](https://img.shields.io/badge/FastAPI-009688)

!\[FAISS](https://img.shields.io/badge/FAISS-Vector\_Search-7C3AED)

!\[Docker](https://img.shields.io/badge/Docker-2496ED)

!\[License](https://img.shields.io/badge/License-MIT-22C55E)



\---



\## ✦ What is it?



\*\*AI Document Assistant\*\* is a Retrieval-Augmented Generation system that lets users interact with PDF documents using natural language.



Instead of sending the entire document to an LLM, it retrieves the most relevant content first and uses that context to generate the answer.



\### Core Pipeline



```text

PDF

&#x20;│

&#x20;▼

PyMuPDF

&#x20;│

&#x20;▼

Chunking

&#x20;│

&#x20;▼

Embeddings

&#x20;│

&#x20;▼

FAISS

&#x20;│

&#x20;▼

Semantic Retrieval

&#x20;│

&#x20;▼

Relevant Context

&#x20;│

&#x20;▼

LLM

&#x20;│

&#x20;▼

Answer + Sources

```



\---



\## ⚡ Features



| Feature | Description |

|---|---|

| 📄 PDF Processing | Extract and index PDF content |

| 🔎 Semantic Search | Find relevant content using embeddings |

| 🧠 RAG | Generate answers from retrieved context |

| 📚 Multi-Document | Query multiple documents |

| 💬 Conversations | Maintain chat history |

| 📍 Sources | Return relevant document pages |

| 🦙 Local AI | Run Qwen3 through llama.cpp |

| 🚀 API | FastAPI REST backend |

| 🐳 Deployment | Docker + Docker Compose |

| 🧪 Testing | Pytest + RAG evaluation |

| ⚙️ CI | GitHub Actions |



\---



\## 🧩 Tech Stack



\*\*Backend\*\*



`Python` · `FastAPI` · `Pydantic` · `SQLAlchemy`



\*\*AI / Retrieval\*\*



`Sentence Transformers` · `FAISS` · `RAG` · `Qwen3` · `llama.cpp`



\*\*Frontend\*\*



`HTML` · `CSS` · `JavaScript`



\*\*Infrastructure\*\*



`Docker` · `GitHub Actions`



\---



\## 🏗️ Architecture



```text

&#x20;                   ┌───────────────┐

&#x20;                   │    Browser    │

&#x20;                   └───────┬───────┘

&#x20;                           │

&#x20;                           ▼

&#x20;                   ┌───────────────┐

&#x20;                   │    FastAPI    │

&#x20;                   └───────┬───────┘

&#x20;                           │

&#x20;             ┌─────────────┴─────────────┐

&#x20;             │                           │

&#x20;             ▼                           ▼

&#x20;       ┌─────────────┐             ┌─────────────┐

&#x20;       │ PDF Pipeline│             │   FAISS     │

&#x20;       │   PyMuPDF   │             │  Retrieval  │

&#x20;       └──────┬──────┘             └──────┬──────┘

&#x20;              │                           │

&#x20;              └─────────────┬─────────────┘

&#x20;                            ▼

&#x20;                     ┌─────────────┐

&#x20;                     │    Qwen3    │

&#x20;                     │  llama.cpp  │

&#x20;                     └──────┬──────┘

&#x20;                            ▼

&#x20;                     Answer + Sources

```



\---



\## 🚀 Quick Start



\### Requirements



\- Python 3.11+

\- Git

\- OpenAI-compatible LLM endpoint



\### Install



```bash

git clone https://github.com/Niharm31/ai-document-assistant.git

cd ai-document-assistant



python -m venv .venv

.venv\\Scripts\\activate



pip install -r requirements.txt

```



\### Configure



Create `.env` from `.env.example`.



For local llama.cpp:



```env

LLM\_BASE\_URL=http://127.0.0.1:8080/v1

LLM\_API\_KEY=local

LLM\_MODEL=your-model-path

```



\### Run



```bash

uvicorn app.main:app --host 0.0.0.0 --port 8000

```



Open:



```text

http://127.0.0.1:8000

```



\---



\## 🦙 Local Qwen3



The application supports local GGUF models through llama.cpp.



```text

Browser

&#x20;  │

&#x20;  ▼

FastAPI :8000

&#x20;  │

&#x20;  ▼

llama.cpp :8080

&#x20;  │

&#x20;  ▼

Qwen3 GGUF

```



\---



\## 🐳 Docker



```bash

docker compose up --build

```



For Docker on Windows connecting to llama.cpp running on the host:



```env

LLM\_BASE\_URL=http://host.docker.internal:8080/v1

```



See \[`DEPLOYMENT.md`](DEPLOYMENT.md) for deployment details.



\---



\## 📊 RAG Evaluation



Retrieval evaluation includes:



\- \*\*Hit@K\*\*

\- \*\*Mean Reciprocal Rank (MRR)\*\*



Run:



```bash

python scripts/evaluate\_rag.py

```



\---



\## 🧪 Testing



```bash

pytest

```



\---



\## 📁 Project Structure



```text

app/

├── api/

├── core/

├── database/

├── models/

└── services/



frontend/

tests/

evals/

scripts/

docs/



Dockerfile

docker-compose.yml

requirements.txt

DEPLOYMENT.md

```



\---



\## 🔭 Roadmap



\- \[ ] Streaming responses

\- \[ ] OCR for scanned PDFs

\- \[ ] Hybrid search

\- \[ ] Reranking

\- \[ ] Authentication

\- \[ ] Cloud deployment

\- \[ ] Distributed vector storage



\---



\## 📄 License



MIT License



\---



\### Nihar Mandal



BTech — Artificial Intelligence \& Machine Learning



\[GitHub](https://github.com/Niharm31) · \[LinkedIn](https://www.linkedin.com/in/nihar-mandal-b512b5288)

