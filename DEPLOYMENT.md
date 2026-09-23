# Deployment Guide

## What this version is designed for

This repository is deployable as a **single-instance container**.

The application stores:
- SQLite data under `data/`
- uploaded PDFs under `data/documents/`
- FAISS index + metadata under `data/vector_store/`
- embedding-model cache under `data/huggingface/`

Therefore the deployment platform must provide a persistent volume if data must survive restarts/redeploys.

The current FAISS implementation is intentionally single-instance. Do not run multiple application workers or multiple replicas with the same local index.

## 1. Local Docker + Great Sage on Windows

Keep your llama.cpp server running on the host at:

```text
http://127.0.0.1:8080/v1
```

Create `.env`:

```env
LLM_BASE_URL=http://host.docker.internal:8080/v1
LLM_API_KEY=local
LLM_MODEL=D:\Great_sage\models\Qwen3-4B-Q4_K_M.gguf
APP_ENV=production
CORS_ORIGINS=*
```

Start:

```powershell
docker compose up --build
```

Open:

```text
http://127.0.0.1:8000
```

## 2. Cloud deployment

A cloud container cannot normally reach `127.0.0.1:8080` on your laptop.

For cloud deployment, use an OpenAI-compatible LLM endpoint reachable by the cloud server and set:

```env
LLM_BASE_URL=https://your-llm-provider.example/v1
LLM_API_KEY=your-secret
LLM_MODEL=your-model
```

Do not commit `.env`.

The cloud platform should provide:

- Docker/container deployment
- A persistent disk/volume mounted at `/app/data`
- A public HTTP port supplied through `$PORT`
- A single application instance/worker
- Environment-variable secret management

## 3. Health checks

Use:

```text
GET /health
```

for liveness.

Use:

```text
GET /ready
```

for a basic readiness check.

## 4. Persistence

Mount a persistent volume to:

```text
/app/data
```

Without persistence, uploaded documents, SQLite records, FAISS indexes, and the downloaded embedding model may disappear when the container is replaced.

## 5. Production security checklist

Before making the site public:

- Set `CORS_ORIGINS` to the exact website origin instead of `*`.
- Use a real secret for `LLM_API_KEY`.
- Keep `.env` out of Git.
- Put authentication in front of the app if documents are private.
- Configure platform-level HTTPS.
- Set upload and request limits at the reverse proxy/platform layer.
- Monitor logs and disk usage.
- Back up `/app/data` if documents matter.

## 6. Scaling limitation

This version is **single-instance deploy-ready**, not horizontally scalable.

The next scaling architecture would replace local SQLite + FAISS + filesystem storage with:

```text
Object Storage
      +
PostgreSQL
      +
Managed Vector Database
      +
Stateless FastAPI instances
```

That should be done before adding multiple replicas.
