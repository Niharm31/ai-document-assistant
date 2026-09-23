from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.core.logging import configure_logging
from app.database.database import Base, engine
from app.api.documents import router as documents_router
from app.api.chat import router as chat_router
from app.services.vector_store import vector_store

configure_logging()

Path(settings.upload_dir).mkdir(parents=True, exist_ok=True)
Path(settings.vector_dir).mkdir(parents=True, exist_ok=True)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Document Assistant",
    version="1.0.0",
    description="A local and deployable RAG document assistant with citations.",
    docs_url="/docs" if settings.app_env != "production" else "/docs",
    redoc_url="/redoc" if settings.app_env != "production" else "/redoc",
)

if settings.cors_origin_list == ["*"]:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(documents_router)
app.include_router(chat_router)

@app.get("/health", tags=["system"])
def health():
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": "1.0.0",
        "environment": settings.app_env,
        "vector_store_loaded": bool(vector_store.metadata),
    }

@app.get("/ready", tags=["system"])
def ready():
    return JSONResponse(
        status_code=200,
        content={
            "status": "ready",
            "vector_store_loaded": bool(vector_store.metadata),
        },
    )

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
