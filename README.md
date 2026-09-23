\# AI Document Assistant



> \*\*Local-first Retrieval-Augmented Generation (RAG) for intelligent PDF question answering.\*\*



Upload PDFs, retrieve relevant context, and ask questions with grounded answers and document sources.



\[!\[Python](https://img.shields.io/badge/Python-3.11%2B-3776AB)](https://www.python.org/)

\[!\[FastAPI](https://img.shields.io/badge/FastAPI-009688)](https://fastapi.tiangolo.com/)

\[!\[FAISS](https://img.shields.io/badge/FAISS-Vector\_Search-7C3AED)](https://github.com/facebookresearch/faiss)

\[!\[Docker](https://img.shields.io/badge/Docker-2496ED)](https://www.docker.com/)

\[!\[License](https://img.shields.io/badge/License-MIT-22C55E)](LICENSE)



\---



\## Overview



\*\*AI Document Assistant\*\* is a RAG application for querying information contained in PDF documents.



Instead of sending an entire document to an LLM, the system retrieves the most relevant passages first and uses them as context for answer generation.



\### Core Workflow



```text

Document

&#x20;  |

&#x20;  v

Text Extraction

&#x20;  |

&#x20;  v

Page-Aware Chunking

&#x20;  |

&#x20;  v

Embeddings

&#x20;  |

&#x20;  v

FAISS Index

&#x20;  |

&#x20;  v

Semantic Retrieval

&#x20;  |

&#x20;  v

Relevant Context

&#x20;  |

&#x20;  v

LLM Generation

&#x20;  |

&#x20;  v

Answer + Sources

```



\---



\## Features



\- PDF upload and text extraction

\- Page-aware document chunking

\- Sentence Transformer embeddings

\- FAISS semantic search

\- Retrieval-Augmented Generation

\- Grounded answers with source pages

\- Multi-document querying

\- Conversation history

\- Document deletion and index rebuilding

\- Local Qwen3 inference through llama.cpp

\- OpenAI-compatible LLM endpoints

\- FastAPI REST API

\- Web-based interface

\- Docker and Docker Compose support

\- GitHub Actions CI

\- Pytest test suite

\- RAG retrieval evaluation



\---



\## Architecture



```text

&#x20;                   +-------------------+

&#x20;                   |      Browser      |

&#x20;                   |   Web Interface   |

&#x20;                   +---------+---------+

&#x20;                             |

&#x20;                             v

&#x20;                   +-------------------+

&#x20;                   |      FastAPI      |

&#x20;                   |      Backend      |

&#x20;                   +---------+---------+

&#x20;                             |

&#x20;              +--------------+--------------+

&#x20;              |                             |

&#x20;              v                             v

&#x20;      +---------------+             +---------------+

&#x20;      | PDF Pipeline  |             |   Retrieval   |

&#x20;      |               |             |               |

&#x20;      |    PyMuPDF    |             |     FAISS     |

&#x20;      |    Chunking   |             |  Embeddings   |

&#x20;      +-------+-------+             +-------+-------+

&#x20;              |                             |

&#x20;              +--------------+--------------+

&#x20;                             |

&#x20;                             v

&#x20;                   +-------------------+

&#x20;                   |        LLM        |

&#x20;                   |  Qwen3 / llama.cpp|

&#x20;                   +---------+---------+

&#x20;                             |

&#x20;                             v

&#x20;                   +-------------------+

&#x20;                   | Grounded Answer   |

&#x20;                   |  + Source Pages   |

&#x20;                   +-------------------+

```



\### Request Flow



1\. Upload a PDF.

2\. Extract text with PyMuPDF.

3\. Split content into page-aware chunks.

4\. Generate semantic embeddings.

5\. Store embeddings in FAISS.

6\. Convert the question into a query embedding.

7\. Retrieve relevant document chunks.

8\. Send the retrieved context to the LLM.

9\. Return the generated answer with document sources.



\---



\## Tech Stack



| Layer | Technologies |

| --- | --- |

| Language | Python 3.11+ |

| Backend | FastAPI, Pydantic |

| PDF Processing | PyMuPDF |

| Embeddings | Sentence Transformers |

| Vector Search | FAISS |

| Database | SQLite, SQLAlchemy |

| LLM | Qwen3, llama.cpp |

| Frontend | HTML, CSS, JavaScript |

| Testing | Pytest |

| Deployment | Docker, Docker Compose |

| CI | GitHub Actions |



\---



\## Quick Start



\### Requirements



\- Python 3.11+

\- Git

\- An OpenAI-compatible LLM endpoint



For local inference:



\- llama.cpp

\- A compatible GGUF model



\### Clone



```bash

git clone https://github.com/Niharm31/ai-document-assistant.git

cd ai-document-assistant

```



\### Create a Virtual Environment



Windows:



```powershell

python -m venv .venv

.venv\\Scripts\\activate

```



Linux/macOS:



```bash

python3 -m venv .venv

source .venv/bin/activate

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\### Configure Environment



Create `.env` from `.env.example`.



Windows:



```powershell

copy .env.example .env

```



Configure:



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



\### Start the Application



```powershell

uvicorn app.main:app --host 0.0.0.0 --port 8000

```



Open:



```text

http://127.0.0.1:8000

```



\---



\## Local LLM with llama.cpp



The application communicates with llama.cpp through its OpenAI-compatible API.



Example:



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



The application connects through:



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



When Docker runs on Windows while llama.cpp runs directly on the host:



```env

LLM\_BASE\_URL=http://host.docker.internal:8080/v1

```



See \[`DEPLOYMENT.md`](DEPLOYMENT.md) for deployment configuration.



\---



\## API



| Endpoint | Method | Description |

| --- | --- | --- |

| `/health` | GET | Application health |

| `/ready` | GET | Readiness status |

| `/api/documents` | GET | List indexed documents |

| `/api/documents/upload` | POST | Upload and index a PDF |

| `/api/documents/{id}` | DELETE | Delete a document |

| `/api/chat` | POST | Ask a document question |

| `/api/chat/{session\_id}/history` | GET | Retrieve conversation history |



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



Evaluation questions:



```text

evals/sample\_questions.json

```



These metrics evaluate retrieval behavior and are not a complete measure of generated-answer quality.



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



GitHub Actions is configured for automated CI checks.



\---



\## Project Structure



```text

ai-document-assistant/

|

+-- app/

|   +-- api/

|   +-- core/

|   +-- database/

|   +-- models/

|   +-- services/

|   +-- main.py

|

+-- frontend/

+-- tests/

+-- evals/

+-- scripts/

+-- docs/

+-- data/

|

+-- .github/

|   +-- workflows/

|

+-- Dockerfile

+-- docker-compose.yml

+-- requirements.txt

+-- pyproject.toml

+-- DEPLOYMENT.md

+-- LICENSE

+-- README.md

```



\---



\## Limitations



\- FAISS storage is local and intended for a single application instance.

\- Embedding generation can be CPU-intensive.

\- Answer quality depends on the selected LLM and retrieved context.

\- Large-scale deployments would require distributed infrastructure.



\---



\## Roadmap



\- \[ ] Streaming LLM responses

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



\## Author



\*\*Nihar Mandal\*\*



BTech — Artificial Intelligence \& Machine Learning



\[GitHub](https://github.com/Niharm31) · \[LinkedIn](https://www.linkedin.com/in/nihar-mandal-b512b5288)

