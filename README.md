\# AI Document Assistant



A local-first \*\*Retrieval-Augmented Generation (RAG)\*\* application for asking questions about PDF documents.



Upload a document, retrieve relevant content, and generate answers grounded in the document.



\## Features



\- PDF upload and text extraction

\- Page-aware document chunking

\- Semantic search with Sentence Transformers

\- FAISS vector retrieval

\- Grounded LLM responses

\- Source-page references

\- Multi-document querying

\- Conversation history

\- Local Qwen3 inference with llama.cpp

\- OpenAI-compatible LLM support

\- FastAPI backend

\- Docker support

\- Automated testing and CI



\## Architecture



```text

PDF

&#x20;↓

PyMuPDF

&#x20;↓

Chunking

&#x20;↓

Embeddings

&#x20;↓

FAISS

&#x20;↓

Semantic Retrieval

&#x20;↓

Relevant Context

&#x20;↓

LLM

&#x20;↓

Answer + Sources

```



\## Tech Stack



\- \*\*Backend:\*\* Python, FastAPI, Pydantic

\- \*\*Document Processing:\*\* PyMuPDF

\- \*\*Embeddings:\*\* Sentence Transformers

\- \*\*Vector Search:\*\* FAISS

\- \*\*Database:\*\* SQLite, SQLAlchemy

\- \*\*LLM:\*\* Qwen3, llama.cpp, OpenAI-compatible APIs

\- \*\*Frontend:\*\* HTML, CSS, JavaScript

\- \*\*Deployment:\*\* Docker, Docker Compose

\- \*\*Testing:\*\* Pytest, GitHub Actions



\## Quick Start



\### 1. Clone



```bash

git clone https://github.com/Niharm31/ai-document-assistant.git

cd ai-document-assistant

```



\### 2. Install



```bash

python -m venv .venv

.venv\\Scripts\\activate

pip install -r requirements.txt

```



\### 3. Configure



Create `.env` from `.env.example` and configure your LLM endpoint.



For local llama.cpp:



```env

LLM\_BASE\_URL=http://127.0.0.1:8080/v1

LLM\_API\_KEY=local

LLM\_MODEL=your-model-path

```



\### 4. Run



```bash

uvicorn app.main:app --host 0.0.0.0 --port 8000

```



Open:



```text

http://127.0.0.1:8000

```



\## Local LLM



The application can use Qwen3 GGUF models through llama.cpp.



```text

Browser

&#x20;  ↓

FastAPI :8000

&#x20;  ↓

llama.cpp :8080

&#x20;  ↓

Qwen3

```



\## Evaluation



The project includes retrieval evaluation using:



\- Hit@K

\- Mean Reciprocal Rank (MRR)



Run:



```bash

python scripts/evaluate\_rag.py

```



\## Testing



```bash

pytest

```



\## Project Structure



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



\## Limitations



FAISS currently uses local storage and is intended for a single application instance. Larger deployments would require distributed storage and infrastructure.



\## Roadmap



\- Streaming responses

\- OCR for scanned PDFs

\- Hybrid search

\- Reranking

\- Authentication

\- Cloud deployment

\- Distributed vector storage



\## License



MIT License.



\## Author



\*\*Nihar Mandal\*\*



BTech — Artificial Intelligence \& Machine Learning



\[GitHub](https://github.com/Niharm31) · \[LinkedIn](https://www.linkedin.com/in/nihar-mandal-b512b5288)

