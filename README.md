<div align="center">



\# AI Document Assistant



\### Local-first Retrieval-Augmented Generation for intelligent document search



Upload documents, retrieve relevant context, and ask questions with grounded, source-aware answers.



<br>



<a href="https://github.com/Niharm31/ai-document-assistant">

&#x20; <img src="https://img.shields.io/github/stars/Niharm31/ai-document-assistant?style=flat-square\&color=7c3aed" alt="GitHub Stars">

</a>

<a href="https://github.com/Niharm31/ai-document-assistant">

&#x20; <img src="https://img.shields.io/github/license/Niharm31/ai-document-assistant?style=flat-square\&color=2563eb" alt="License">

</a>

<a href="https://www.python.org/">

&#x20; <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square\&logo=python\&logoColor=white" alt="Python">

</a>

<a href="https://fastapi.tiangolo.com/">

&#x20; <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square\&logo=fastapi\&logoColor=white" alt="FastAPI">

</a>

<a href="https://github.com/facebookresearch/faiss">

&#x20; <img src="https://img.shields.io/badge/FAISS-Vector%20Search-7c3aed?style=flat-square" alt="FAISS">

</a>

<a href="https://www.docker.com/">

&#x20; <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square\&logo=docker\&logoColor=white" alt="Docker">

</a>



<br><br>



<a href="#overview">Overview</a>

\&nbsp;\&nbsp;•\&nbsp;\&nbsp;

<a href="#architecture">Architecture</a>

\&nbsp;\&nbsp;•\&nbsp;\&nbsp;

<a href="#quick-start">Quick Start</a>

\&nbsp;\&nbsp;•\&nbsp;\&nbsp;

<a href="#api">API</a>

\&nbsp;\&nbsp;•\&nbsp;\&nbsp;

<a href="#roadmap">Roadmap</a>



</div>



\---



\## Overview



\*\*AI Document Assistant\*\* is a local-first RAG application that allows users to ask questions about their PDF documents.



The system combines document processing, semantic search, vector retrieval, and LLM generation to produce answers grounded in the uploaded documents.



\### Core workflow



```text

Document

&#x20;  │

&#x20;  ▼

Text Extraction

&#x20;  │

&#x20;  ▼

Page-Aware Chunking

&#x20;  │

&#x20;  ▼

Embeddings

&#x20;  │

&#x20;  ▼

FAISS Index

&#x20;  │

&#x20;  ▼

Semantic Retrieval

&#x20;  │

&#x20;  ▼

Relevant Context

&#x20;  │

&#x20;  ▼

LLM Generation

&#x20;  │

&#x20;  ▼

Answer + Sources

```



\---



\## Key Features



<table>

<tr>

<td width="50%">



\### Document Intelligence



\- PDF upload

\- Text extraction

\- Page-aware chunking

\- Semantic embeddings

\- Multi-document search

\- Document deletion



</td>

<td width="50%">



\### AI \& Retrieval



\- RAG pipeline

\- FAISS vector search

\- Grounded responses

\- Source-page references

\- Conversation history

\- Local LLM inference



</td>

</tr>

<tr>

<td>



\### Developer Experience



\- FastAPI REST API

\- Automated tests

\- RAG evaluation utilities

\- Configurable environment

\- Health and readiness endpoints



</td>

<td>



\### Deployment



\- Docker

\- Docker Compose

\- GitHub Actions

\- Persistent application data

\- OpenAI-compatible LLM endpoints



</td>

</tr>

</table>



\---



\## Architecture



```text

&#x20;                        ┌──────────────────────┐

&#x20;                        │       Browser        │

&#x20;                        │    Web Interface     │

&#x20;                        └──────────┬───────────┘

&#x20;                                   │

&#x20;                                   ▼

&#x20;                        ┌──────────────────────┐

&#x20;                        │       FastAPI        │

&#x20;                        │      REST API        │

&#x20;                        └──────────┬───────────┘

&#x20;                                   │

&#x20;                ┌──────────────────┴──────────────────┐

&#x20;                │                                     │

&#x20;                ▼                                     ▼

&#x20;       ┌─────────────────┐                   ┌─────────────────┐

&#x20;       │  PDF Pipeline   │                   │    Retrieval    │

&#x20;       │                 │                   │                 │

&#x20;       │    PyMuPDF      │                   │     FAISS       │

&#x20;       │    Chunking     │                   │    Embeddings   │

&#x20;       └────────┬────────┘                   └────────┬────────┘

&#x20;                │                                     │

&#x20;                └────────────────┬────────────────────┘

&#x20;                                 │

&#x20;                                 ▼

&#x20;                        ┌──────────────────────┐

&#x20;                        │      LLM Layer       │

&#x20;                        │                      │

&#x20;                        │ Qwen3 / llama.cpp /  │

&#x20;                        │ OpenAI-compatible    │

&#x20;                        └──────────┬───────────┘

&#x20;                                   │

&#x20;                                   ▼

&#x20;                        ┌──────────────────────┐

&#x20;                        │ Grounded Response    │

&#x20;                        │   + Source Pages     │

&#x20;                        └──────────────────────┘

```



\### Request flow



1\. A PDF is uploaded.

2\. Text is extracted with PyMuPDF.

3\. Content is split into page-aware chunks.

4\. Sentence Transformers generates embeddings.

5\. Embeddings are stored in FAISS.

6\. A user question is converted into a query embedding.

7\. Relevant chunks are retrieved.

8\. Retrieved context is supplied to the LLM.

9\. The application returns the generated answer with document sources.



\---



\## Technology Stack



| Category | Technologies |

|---|---|

| Language | Python 3.11+ |

| API | FastAPI, Pydantic |

| PDF Processing | PyMuPDF |

| Embeddings | Sentence Transformers |

| Vector Search | FAISS |

| Database | SQLite, SQLAlchemy |

| LLM | Qwen3, llama.cpp |

| Frontend | HTML, CSS, JavaScript |

| Testing | Pytest |

| Containers | Docker, Docker Compose |

| CI | GitHub Actions |



\---



\## Quick Start



\### Requirements



\- Python 3.11+

\- Git

\- An OpenAI-compatible LLM endpoint



For fully local inference:



\- llama.cpp

\- A compatible GGUF model



\### Clone



```bash

git clone https://github.com/Niharm31/ai-document-assistant.git

cd ai-document-assistant

```



\### Environment



Create a virtual environment:



```powershell

python -m venv .venv

.venv\\Scripts\\activate

```



Install dependencies:



```powershell

pip install -r requirements.txt

```



Create your environment file:



```powershell

copy .env.example .env

```



Configure the LLM:



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



> Keep `.env` private. Never commit credentials or API keys.



\### Run



Start the application:



```powershell

uvicorn app.main:app --host 0.0.0.0 --port 8000

```



Open:



\*\*http://127.0.0.1:8000\*\*



\---



\## Local LLM



The application supports OpenAI-compatible LLM servers.



For local Qwen3 inference with llama.cpp:



```powershell

llama-server.exe `

&#x20; -m "D:\\path\\to\\Qwen3-4B-Q4\_K\_M.gguf" `

&#x20; --host 127.0.0.1 `

&#x20; --port 8080

```



Verify the server:



```powershell

curl http://127.0.0.1:8080/health

```



Expected:



```json

{"status":"ok"}

```



The application then communicates with the model through:



```text

http://127.0.0.1:8080/v1

```



\---



\## Docker



Build:



```bash

docker build -t ai-document-assistant .

```



Run:



```bash

docker run --env-file .env -p 8000:8000 ai-document-assistant

```



Or:



```bash

docker compose up --build

```



When llama.cpp is running on the Windows host while the application runs inside Docker:



```env

LLM\_BASE\_URL=http://host.docker.internal:8080/v1

```



For deployment configuration, see \[`DEPLOYMENT.md`](DEPLOYMENT.md).



\---



\## API



| Endpoint | Method | Description |

|---|:---:|---|

| `/health` | `GET` | Application health |

| `/ready` | `GET` | Readiness status |

| `/api/documents` | `GET` | List indexed documents |

| `/api/documents/upload` | `POST` | Upload and index a PDF |

| `/api/documents/{id}` | `DELETE` | Delete a document |

| `/api/chat` | `POST` | Ask a document question |

| `/api/chat/{session\_id}/history` | `GET` | Retrieve conversation history |



\---



\## Evaluation



The repository includes a lightweight retrieval evaluation utility.



Metrics include:



\- \*\*Hit@K\*\*

\- \*\*Mean Reciprocal Rank (MRR)\*\*



Run:



```bash

python scripts/evaluate\_rag.py

```



Evaluation questions are stored in:



```text

evals/sample\_questions.json

```



These metrics measure retrieval behavior and are not intended to represent complete end-to-end answer quality.



\---



\## Testing



Run the test suite:



```bash

pytest

```



Compile the application:



```bash

python -m compileall app

```



Continuous integration is configured through GitHub Actions.



\---



\## Project Structure



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



\## Limitations



\- FAISS storage is local and intended for a single application instance.

\- Embedding generation can be CPU-intensive.

\- Response quality depends on the selected LLM and retrieved context.

\- Large-scale deployments would require distributed infrastructure.



\---



\## Roadmap



\- \[ ] Streaming responses

\- \[ ] OCR for scanned PDFs

\- \[ ] Hybrid keyword + vector retrieval

\- \[ ] Reranking

\- \[ ] Authentication

\- \[ ] Background document processing

\- \[ ] Cloud object storage

\- \[ ] Distributed vector storage

\- \[ ] Advanced RAG evaluation

\- \[ ] Observability and tracing



\---



\## License



This project is licensed under the \[MIT License](LICENSE).



\---



<div align="center">



\### Built by Nihar Mandal



BTech — Artificial Intelligence \& Machine Learning



<a href="https://github.com/Niharm31">GitHub</a>

\&nbsp;•\&nbsp;

<a href="https://www.linkedin.com/in/nihar-mandal-b512b5288">LinkedIn</a>



</div>

