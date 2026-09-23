\# AI Document Assistant



> \*\*A local-first RAG system for intelligent PDF question answering.\*\*



Upload a PDF → retrieve the relevant context → ask questions → get grounded answers with source pages.



<p align="center">



!\[Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

!\[FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)

!\[FAISS](https://img.shields.io/badge/FAISS-Vector\_Search-00A67E?style=for-the-badge)

!\[RAG](https://img.shields.io/badge/RAG-LLM-8B5CF6?style=for-the-badge)

!\[Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)



</p>



\---



\## Overview



\*\*AI Document Assistant\*\* combines semantic search and Large Language Models to answer questions directly from your documents.



Instead of sending an entire PDF to an LLM, the system retrieves the most relevant passages first and uses them as context for generation.



```text

PDF

&#x20;↓

PyMuPDF

&#x20;↓

Smart Chunking

&#x20;↓

Embeddings

&#x20;↓

FAISS

&#x20;↓

Semantic Retrieval

&#x20;↓

LLM

&#x20;↓

Answer + Sources

```



\---



\## ✦ Features



| | Capability |

|---|---|

| ◈ | PDF upload \& text extraction |

| ◈ | Page-aware chunking |

| ◈ | Semantic vector search |

| ◈ | FAISS retrieval |

| ◈ | Grounded RAG responses |

| ◈ | Multi-document querying |

| ◈ | Conversation history |

| ◈ | Source page references |

| ◈ | Local Qwen3 / llama.cpp |

| ◈ | Docker \& GitHub Actions |



\---



\## ⚙️ Architecture



```text

&#x20;                 ┌─────────────────┐

&#x20;                 │     Browser     │

&#x20;                 └────────┬────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;                 ┌─────────────────┐

&#x20;                 │     FastAPI     │

&#x20;                 └───────┬─────────┘

&#x20;                         │

&#x20;            ┌────────────┴────────────┐

&#x20;            ▼                         ▼

&#x20;     ┌─────────────┐           ┌─────────────┐

&#x20;     │ PDF Pipeline│           │   FAISS      │

&#x20;     │  PyMuPDF    │           │  Retrieval   │

&#x20;     └──────┬──────┘           └──────┬──────┘

&#x20;            │                         │

&#x20;            └───────────┬─────────────┘

&#x20;                        ▼

&#x20;                 ┌─────────────┐

&#x20;                 │     LLM     │

&#x20;                 │ Qwen3 / API │

&#x20;                 └──────┬──────┘

&#x20;                        ▼

&#x20;                Grounded Answer

&#x20;                  + Sources

```



\---



\## 🧠 Tech Stack



\*\*Backend\*\*



`Python` · `FastAPI` · `SQLAlchemy` · `SQLite` · `PyMuPDF`



\*\*AI / Retrieval\*\*



`Sentence Transformers` · `FAISS` · `RAG` · `Qwen3` · `llama.cpp`



\*\*Frontend\*\*



`HTML` · `CSS` · `JavaScript`



\*\*DevOps\*\*



`Docker` · `Docker Compose` · `GitHub Actions` · `Pytest`



\---



\## 🚀 Quick Start



\### 1. Clone



```bash

git clone https://github.com/Niharm31/ai-document-assistant.git

cd ai-document-assistant

```



\### 2. Install



```powershell

python -m venv .venv

.venv\\Scripts\\activate

pip install -r requirements.txt

```



\### 3. Configure



Create `.env` from `.env.example`.



For a local llama.cpp server:



```env

LLM\_BASE\_URL=http://127.0.0.1:8080/v1

LLM\_API\_KEY=local

LLM\_MODEL=your-model-path

```



\### 4. Run



```powershell

uvicorn app.main:app --host 0.0.0.0 --port 8000

```



Open:



\*\*http://127.0.0.1:8000\*\*



\---



\## 🐳 Docker



```bash

docker compose up --build

```



For Docker connecting to llama.cpp running on the Windows host:



```env

LLM\_BASE\_URL=http://host.docker.internal:8080/v1

```



See \[`DEPLOYMENT.md`](DEPLOYMENT.md) for deployment details.



\---



\## 📊 Evaluation



The repository includes a lightweight retrieval evaluation utility using:



\- \*\*Hit@K\*\*

\- \*\*Mean Reciprocal Rank (MRR)\*\*



Run:



```bash

python scripts/evaluate\_rag.py

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



\## 🔮 Roadmap



\- \[ ] Streaming responses

\- \[ ] OCR for scanned PDFs

\- \[ ] Hybrid search

\- \[ ] Reranking

\- \[ ] Authentication

\- \[ ] Cloud deployment

\- \[ ] Distributed vector storage



\---



\## License



MIT



\---



\## Author



\*\*Nihar Mandal\*\*



BTech — Artificial Intelligence \& Machine Learning



\[GitHub](https://github.com/Niharm31) · \[LinkedIn](https://www.linkedin.com/in/nihar-mandal-b512b5288)

