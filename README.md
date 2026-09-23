\# AI Document Assistant



A local-first Retrieval-Augmented Generation (RAG) application for asking grounded questions about PDF documents.



The application extracts text from uploaded PDFs, creates page-aware chunks, generates semantic embeddings, retrieves relevant passages using FAISS, and passes the retrieved context to an OpenAI-compatible Large Language Model (LLM).



It can run entirely locally with a GGUF model served through `llama.cpp`, or connect to a compatible remote LLM endpoint.



\---



\## Features



\- PDF upload and text extraction

\- Page-aware document chunking

\- Semantic embeddings with Sentence Transformers

\- FAISS vector search

\- Retrieval-Augmented Generation (RAG)

\- Grounded question answering

\- Page-level source references

\- Multi-document querying

\- Conversation history

\- Document deletion and index rebuilding

\- Local LLM inference with `llama.cpp`

\- Qwen3 GGUF model support

\- OpenAI-compatible LLM endpoints

\- FastAPI REST API

\- Web-based frontend

\- Docker support

\- Docker Compose configuration

\- Persistent application data

\- Automated tests with Pytest

\- GitHub Actions CI

\- RAG retrieval evaluation utilities

\- Health and readiness endpoints

\- Configurable upload limits and CORS



\---



\## Demo



The application provides a browser-based interface where users can:



1\. Upload PDF documents.

2\. Select one or multiple documents.

3\. Ask questions about their contents.

4\. Retrieve relevant document passages.

5\. Generate answers using the configured LLM.

6\. View the document pages used as sources.

7\. Continue conversations using session history.



\---



\## How It Works



```text

PDF

&#x20;│

&#x20;▼

PyMuPDF

&#x20;│

&#x20;▼

Page-Aware Chunking

&#x20;│

&#x20;▼

Sentence Transformers

&#x20;│

&#x20;▼

FAISS Vector Index

&#x20;│

&#x20;▼

User Question

&#x20;│

&#x20;▼

Semantic Retrieval

&#x20;│

&#x20;▼

Relevant Document Context

&#x20;│

&#x20;▼

Qwen3 / OpenAI-Compatible LLM

&#x20;│

&#x20;▼

Grounded Answer

&#x20;+ Source Pages

```



The system follows a Retrieval-Augmented Generation architecture rather than sending the entire document directly to the language model.



This allows the application to retrieve the most relevant sections of a document before generating an answer.



\---



\## Architecture



```text

&#x20;                        ┌─────────────────────┐

&#x20;                        │      Web Browser     │

&#x20;                        │    HTML / CSS / JS   │

&#x20;                        └──────────┬──────────┘

&#x20;                                   │

&#x20;                                   ▼

&#x20;                        ┌─────────────────────┐

&#x20;                        │       FastAPI       │

&#x20;                        │      REST API        │

&#x20;                        └───────┬───────┬─────┘

&#x20;                                │       │

&#x20;                      Documents │       │ Questions

&#x20;                                │       │

&#x20;                                ▼       ▼

&#x20;                       ┌──────────┐  ┌──────────────┐

&#x20;                       │ PyMuPDF  │  │  Retrieval   │

&#x20;                       │ PDF Text │  │    FAISS     │

&#x20;                       └────┬─────┘  └──────┬───────┘

&#x20;                            │               │

&#x20;                            ▼               ▼

&#x20;                      ┌──────────┐   ┌──────────────┐

&#x20;                      │ Chunking │   │ Relevant PDF │

&#x20;                      │ + Pages  │   │   Context    │

&#x20;                      └────┬─────┘   └──────┬───────┘

&#x20;                           │                 │

&#x20;                           ▼                 │

&#x20;                   ┌────────────────┐        │

&#x20;                   │   Sentence     │        │

&#x20;                   │  Transformers  │        │

&#x20;                   └───────┬────────┘        │

&#x20;                           │                 │

&#x20;                           ▼                 ▼

&#x20;                        ┌────────────────────────┐

&#x20;                        │    OpenAI-Compatible   │

&#x20;                        │          LLM           │

&#x20;                        │  Qwen3 / llama.cpp     │

&#x20;                        └───────────┬────────────┘

&#x20;                                    │

&#x20;                                    ▼

&#x20;                             Grounded Answer

&#x20;                             + Source Pages

```



A more detailed architecture diagram is available in:



```text

docs/architecture.md

docs/architecture.svg

```



\---



\## Technology Stack



\### Backend



\- Python 3.11+

\- FastAPI

\- Pydantic

\- SQLAlchemy

\- SQLite

\- PyMuPDF



\### AI / Retrieval



\- Sentence Transformers

\- FAISS

\- Retrieval-Augmented Generation

\- Semantic vector search

\- Qwen3

\- GGUF

\- llama.cpp



\### Frontend



\- HTML

\- CSS

\- JavaScript



\### Testing



\- Pytest

\- RAG retrieval evaluation



\### DevOps



\- Docker

\- Docker Compose

\- GitHub Actions

\- Production-oriented configuration



\---



\## Project Structure



```text

ai-document-assistant/

│

├── app/

│   ├── api/

│   │   ├── \_\_init\_\_.py

│   │   ├── chat.py

│   │   └── documents.py

│   │

│   ├── core/

│   │   ├── \_\_init\_\_.py

│   │   ├── config.py

│   │   └── logging.py

│   │

│   ├── database/

│   │   ├── \_\_init\_\_.py

│   │   ├── database.py

│   │   └── models.py

│   │

│   ├── models/

│   │   ├── \_\_init\_\_.py

│   │   └── document.py

│   │

│   ├── services/

│   │   ├── \_\_init\_\_.py

│   │   ├── chunker.py

│   │   ├── document\_loader.py

│   │   ├── embeddings.py

│   │   ├── llm.py

│   │   └── vector\_store.py

│   │

│   └── main.py

│

├── frontend/

│   ├── index.html

│   ├── style.css

│   └── app.js

│

├── tests/

│   ├── test\_api.py

│   └── test\_chunker.py

│

├── evals/

│   └── sample\_questions.json

│

├── scripts/

│   └── evaluate\_rag.py

│

├── docs/

│   ├── architecture.md

│   └── architecture.svg

│

├── data/

│   ├── documents/

│   └── vector\_store/

│

├── .github/

│   └── workflows/

│       └── tests.yml

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



\# Local Setup



\## Requirements



\- Python 3.11 or newer

\- Git

\- pip

\- An OpenAI-compatible LLM endpoint



For fully local inference:



\- llama.cpp

\- A compatible GGUF model

\- Sufficient RAM/CPU resources for the selected model



\---



\## Clone the Repository



```bash

git clone https://github.com/Niharm31/ai-document-assistant.git

cd ai-document-assistant

```



\---



\## Create a Virtual Environment



\### Windows



```powershell

python -m venv .venv

.venv\\Scripts\\activate

```



\### Linux / macOS



```bash

python3 -m venv .venv

source .venv/bin/activate

```



\---



\## Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\## Configure Environment Variables



Copy `.env.example` to `.env`.



\### Windows



```powershell

copy .env.example .env

```



\### Linux / macOS



```bash

cp .env.example .env

```



Configure the LLM connection.



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



Do not commit `.env` to Git.



\---



\# Running with llama.cpp



The application communicates with llama.cpp through its OpenAI-compatible API.



Example:



```powershell

llama-server.exe `

&#x20; -m "D:\\path\\to\\Qwen3-4B-Q4\_K\_M.gguf" `

&#x20; --host 127.0.0.1 `

&#x20; --port 8080

```



Once the model finishes loading, check its health:



```powershell

curl http://127.0.0.1:8080/health

```



Expected response:



```json

{

&#x20; "status": "ok"

}

```



You can also check the available model:



```powershell

curl http://127.0.0.1:8080/v1/models

```



\---



\# Start the Application



From the project directory:



```powershell

uvicorn app.main:app --host 0.0.0.0 --port 8000

```



The application will be available at:



```text

http://127.0.0.1:8000

```



Open that address in your browser.



\---



\# Local Architecture



When running locally with llama.cpp:



```text

Browser

&#x20;  │

&#x20;  │ HTTP :8000

&#x20;  ▼

FastAPI

&#x20;  │

&#x20;  │ OpenAI-compatible API

&#x20;  │ :8080

&#x20;  ▼

llama.cpp

&#x20;  │

&#x20;  ▼

Qwen3 GGUF

```



The browser communicates with FastAPI.



FastAPI communicates with the LLM.



The browser does not need direct access to the LLM server.



\---



\# Docker



\## Build the Image



```bash

docker build -t ai-document-assistant .

```



\## Run the Container



```bash

docker run --env-file .env -p 8000:8000 ai-document-assistant

```



Open:



```text

http://127.0.0.1:8000

```



\---



\## Docker Compose



Start the application:



```bash

docker compose up --build

```



Stop it:



```bash

docker compose down

```



\---



\## Docker + Local llama.cpp on Windows



If the application is running inside Docker while llama.cpp is running directly on Windows, use:



```env

LLM\_BASE\_URL=http://host.docker.internal:8080/v1

```



Do not use:



```env

LLM\_BASE\_URL=http://127.0.0.1:8080/v1

```



inside the container because `127.0.0.1` would refer to the container itself.



See \[`DEPLOYMENT.md`](DEPLOYMENT.md) for additional deployment information.



\---



\# API



\## Health Check



```http

GET /health

```



Used to determine whether the application is running.



\---



\## Readiness Check



```http

GET /ready

```



Used to check whether the application is ready to handle requests.



\---



\## List Documents



```http

GET /api/documents

```



Returns indexed documents.



\---



\## Upload Document



```http

POST /api/documents/upload

```



Uploads and indexes a PDF document.



\---



\## Delete Document



```http

DELETE /api/documents/{document\_id}

```



Deletes a document and rebuilds the local vector index.



\---



\## Ask a Question



```http

POST /api/chat

```



Sends a question through the retrieval and generation pipeline.



\---



\## Conversation History



```http

GET /api/chat/{session\_id}/history

```



Retrieves conversation history for a session.



\---



\# RAG Evaluation



The repository includes a small evaluation framework for testing retrieval behavior.



Sample questions are located at:



```text

evals/sample\_questions.json

```



Run the evaluation script:



```bash

python scripts/evaluate\_rag.py

```



The evaluation utility reports retrieval-oriented metrics including:



\- Hit@K

\- Mean Reciprocal Rank (MRR)



These metrics measure retrieval performance. They should not be interpreted as a complete evaluation of generated-answer correctness.



\---



\# Testing



Run the automated tests:



```bash

pytest

```



Compile the application source:



```bash

python -m compileall app

```



The repository also includes a GitHub Actions workflow for automated CI checks.



\---



\# Data and Persistence



Application data is stored under:



```text

data/

```



The directory contains:



```text

data/

├── documents/

└── vector\_store/

```



These directories are intentionally excluded from version control except for their `.gitkeep` files.



For Docker deployments, persistent storage should be mounted to `/app/data`.



\---



\# Security and Configuration



The application supports configurable:



\- LLM endpoints

\- API keys

\- CORS origins

\- Upload size limits

\- Embedding models

\- Retrieval depth

\- Application environment



Sensitive configuration belongs in `.env`.



The repository intentionally does not contain local credentials or API keys.



\---



\# Limitations



The current architecture is designed primarily for local and single-instance deployment.



\### Vector Storage



FAISS is maintained locally by the application process. It is not intended for horizontally scaled multi-instance deployments without additional architecture.



\### Embeddings



Embedding generation can be CPU-intensive on systems without hardware acceleration.



\### LLM Quality



Generated answers depend on:



\- The selected LLM

\- Retrieval quality

\- Document structure

\- Chunking strategy

\- Embedding quality

\- Available context



\### Large-Scale Deployment



A larger production deployment would typically move persistent infrastructure to dedicated services.



\---



\# Potential Production Architecture



For a horizontally scalable deployment, the architecture could evolve toward:



```text

&#x20;               ┌───────────────┐

&#x20;               │   Frontend    │

&#x20;               └───────┬───────┘

&#x20;                       │

&#x20;                       ▼

&#x20;               ┌───────────────┐

&#x20;               │ Load Balancer │

&#x20;               └───────┬───────┘

&#x20;                       │

&#x20;             ┌─────────┴─────────┐

&#x20;             ▼                   ▼

&#x20;       ┌───────────┐       ┌───────────┐

&#x20;       │ FastAPI   │       │ FastAPI   │

&#x20;       │ Instance  │       │ Instance  │

&#x20;       └─────┬─────┘       └─────┬─────┘

&#x20;             │                   │

&#x20;             └─────────┬─────────┘

&#x20;                       │

&#x20;         ┌─────────────┼─────────────┐

&#x20;         ▼             ▼             ▼

&#x20;   PostgreSQL    Vector Database   Object Storage

&#x20;         │             │             │

&#x20;         └─────────────┼─────────────┘

&#x20;                       │

&#x20;                       ▼

&#x20;                 LLM Inference

```



Potential components include:



\- PostgreSQL for metadata

\- Object storage for documents

\- A distributed or managed vector database

\- Dedicated LLM inference infrastructure

\- Background workers for document processing

\- Observability and tracing



\---



\# Future Improvements



Potential future additions include:



\- Streaming LLM responses

\- OCR for scanned PDFs

\- Hybrid keyword + vector retrieval

\- Reranking models

\- Authentication and user accounts

\- Background document processing

\- Cloud object storage

\- PostgreSQL-backed metadata

\- Distributed vector storage

\- Improved evaluation datasets

\- Answer-quality evaluation

\- Observability and tracing

\- Rate limiting

\- Role-based access control

\- Cloud deployment templates



\---



\# License



This project is licensed under the MIT License.



See \[`LICENSE`](LICENSE) for the full license text.



\---



\# Author



\*\*Nihar Mandal\*\*



BTech — Artificial Intelligence \& Machine Learning



GitHub:  

https://github.com/Niharm31



LinkedIn:  

https://www.linkedin.com/in/nihar-mandal-b512b5288

