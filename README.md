\# AI Document Assistant



> \*\*Local-first RAG for intelligent PDF question answering.\*\*



Upload a PDF → retrieve relevant context → ask questions → get grounded answers with source pages.



<p align="center">



\[!\[Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)

\[!\[FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com/)

\[!\[FAISS](https://img.shields.io/badge/FAISS-Vector\_Search-00A67E?style=for-the-badge)](https://github.com/facebookresearch/faiss)

\[!\[Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)](https://www.docker.com/)



</p>



\---



\## Overview



\*\*AI Document Assistant\*\* is a Retrieval-Augmented Generation system designed to answer questions from PDF documents.



Instead of sending an entire document to an LLM, it:



```text

PDF

&#x20;↓

Text Extraction

&#x20;↓

Smart Chunking

&#x20;↓

Embeddings

&#x20;↓

FAISS Retrieval

&#x20;↓

Relevant Context

&#x20;↓

LLM

&#x20;↓

Grounded Answer + Sources

```



This makes the application suitable for document search, knowledge retrieval, and local AI workflows.



\---



\## ✦ Features



\- PDF upload and text extraction

\- Page-aware document chunking

\- Semantic embeddings

\- FAISS vector search

\- Retrieval-Augmented Generation

\- Grounded answers with source pages

\- Multi-document querying

\- Conversation history

\- Local Qwen3 / llama.cpp support

\- OpenAI-compatible LLM endpoints

\- FastAPI backend

\- Web-based interface

\- Docker support

\- GitHub Actions CI

\- Pytest test suite

\- RAG retrieval evaluation



\---



\## ⚙️ Architecture



```text

&#x20;                   ┌──────────────────┐

&#x20;                   │     Browser      │

&#x20;                   │   HTML / CSS / JS│

&#x20;                   └────────┬─────────┘

&#x20;                            │

&#x20;                            ▼

&#x20;                   ┌──────────────────┐

&#x20;                   │     FastAPI      │

&#x20;                   │      Backend     │

&#x20;                   └────────┬─────────┘

&#x20;                            │

&#x20;                ┌───────────┴───────────┐

&#x20;                │                       │

&#x20;                ▼                       ▼

&#x20;         ┌─────────────┐        ┌─────────────┐

&#x20;         │ PDF Pipeline│        │    FAISS    │

&#x20;         │   PyMuPDF   │        │  Retrieval  │

&#x20;         └──────┬──────┘        └──────┬──────┘

&#x20;                │                      │

&#x20;                └──────────┬───────────┘

&#x20;                           ▼

&#x20;                   ┌──────────────┐

&#x20;                   │     LLM      │

&#x20;                   │ Qwen3 / API  │

&#x20;                   └──────┬───────┘

&#x20;                          ▼

&#x20;                 Grounded Answer

&#x20;                   + Source Pages

```



\---



\## 🧠 Tech Stack



| Layer | Technologies |

|---|---|

| Backend | Python, FastAPI, Pydantic |

| PDF Processing | PyMuPDF |

| Retrieval | FAISS, Sentence Transformers |

| Database | SQLite, SQLAlchemy |

| LLM | Qwen3, llama.cpp, OpenAI-compatible APIs |

| Frontend | HTML, CSS, JavaScript |

| Testing | Pytest |

| DevOps | Docker, Docker Compose, GitHub Actions |



\---



\## 🚀 Quick Start



\### Requirements



\- Python 3.11+

\- Git

\- An OpenAI-compatible LLM endpoint



For fully local inference:



\- llama.cpp

\- A compatible GGUF model



\### 1. Clone



```bash

git clone https://github.com/Niharm31/ai-document-assistant.git

cd ai-document-assistant

```



\### 2. Create a virtual environment



\*\*Windows\*\*



```powershell

python -m venv .venv

.venv\\Scripts\\activate

```



\*\*Linux / macOS\*\*



```bash

python3 -m venv .venv

source .venv/bin/activate

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Configure `.env`



Create `.env` from `.env.example`.



For a local llama.cpp server:



```env

LLM\_BASE\_URL=http://127.0.0.1:8080/v1

LLM\_API\_KEY=local

LLM\_MODEL=your-model-path



APP\_ENV=production

EMBEDDING\_MODEL=sentence-transformers/all-MiniLM-L6-v2

TOP\_K=5

MAX\_UPLOAD\_MB=20

CORS\_ORIGINS=\*

```



> Keep `.env` private. Never commit API keys or credentials.



\### 5. Start the application



```powershell

uvicorn app.main:app --host 0.0.0.0 --port 8000

```



Open:



```text

http://127.0.0.1:8000

```



\---



\## 🦙 Local LLM with llama.cpp



Example using a Qwen3 GGUF model:



```powershell

llama-server.exe `

&#x20; -m "D:\\path\\to\\Qwen3-4B-Q4\_K\_M.gguf" `

&#x20; --host 127.0.0.1 `

&#x20; --port 8080

```



Check the server:



```powershell

curl http://127.0.0.1:8080/health

```



Expected:



```json

{"status":"ok"}

```



Check the loaded model:



```powershell

curl http://127.0.0.1:8080/v1/models

```



The application then communicates with llama.cpp through its OpenAI-compatible API.



\---



\## 🐳 Docker



Build:



```bash

docker build -t ai-document-assistant .

```



Run:



```bash

docker run --env-file .env -p 8000:8000 ai-document-assistant

```



Or use Docker Compose:



```bash

docker compose up --build

```



When Docker runs on Windows while llama.cpp runs directly on the host:



```env

LLM\_BASE\_URL=http://host.docker.internal:8080/v1

```



See \[`DEPLOYMENT.md`](DEPLOYMENT.md) for deployment configuration.



\---



\## 📡 API



| Endpoint | Method | Description |

|---|---|---|

| `/health` | `GET` | Application health |

| `/ready` | `GET` | Readiness status |

| `/api/documents` | `GET` | List documents |

| `/api/documents/upload` | `POST` | Upload a PDF |

| `/api/documents/{id}` | `DELETE` | Delete a document |

| `/api/chat` | `POST` | Ask a document question |

| `/api/chat/{session\_id}/history` | `GET` | Get conversation history |



\---



\## 📊 Evaluation



The repository includes a lightweight retrieval evaluation utility.



Metrics include:



\- \*\*Hit@K\*\*

\- \*\*Mean Reciprocal Rank (MRR)\*\*



Run:



```bash

python scripts/evaluate\_rag.py

```



Evaluation data:



```text

evals/sample\_questions.json

```



These metrics evaluate retrieval behavior and should not be treated as a complete measurement of generated-answer quality.



\---



\## 🧪 Testing



Run the test suite:



```bash

pytest

```



Compile the application:



```bash

python -m compileall app

```



GitHub Actions is configured to run automated project checks.



\---



\## 📁 Project Structure



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

├── .github/

│   └── workflows/

│

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── pyproject.toml

├── DEPLOYMENT.md

├── LICENSE

└── README.md

```



\---



\## 🔭 Roadmap



\- \[ ] Streaming LLM responses

\- \[ ] OCR for scanned PDFs

\- \[ ] Hybrid keyword + vector search

\- \[ ] Reranking

\- \[ ] Authentication

\- \[ ] Background document processing

\- \[ ] Cloud object storage

\- \[ ] Distributed vector storage

\- \[ ] Advanced RAG evaluation

\- \[ ] Observability and tracing



\---



\## ⚠️ Current Limitations



\- FAISS storage is local and intended for a single application instance.

\- Embedding generation can be CPU-intensive.

\- Answer quality depends on the selected LLM and retrieved context.

\- Large-scale deployments would benefit from distributed infrastructure.



\---



\## 📄 License



MIT License — see \[`LICENSE`](LICENSE).



\---



\## Author



\*\*Nihar Mandal\*\*



BTech — Artificial Intelligence \& Machine Learning



\[GitHub](https://github.com/Niharm31) · \[LinkedIn](https://www.linkedin.com/in/nihar-mandal-b512b5288)



\---



<p align="center">

Built with Python, FastAPI, FAISS and local LLM inference.

</p>

