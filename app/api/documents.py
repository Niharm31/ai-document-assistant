from pathlib import Path
from uuid import uuid4
import logging
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.core.config import settings
from app.database.database import get_db
from app.database.models import Document
from app.models.document import DocumentOut
from app.services.chunker import chunk_pages
from app.services.document_loader import extract_pdf
from app.services.vector_store import vector_store

router = APIRouter(prefix="/api/documents", tags=["documents"])
logger = logging.getLogger(__name__)

@router.post("/upload", response_model=DocumentOut)
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    filename = Path(file.filename or "document.pdf").name
    if file.content_type != "application/pdf" and not filename.lower().endswith(".pdf"):
        raise HTTPException(400, "Only PDF files are supported.")

    content = await file.read()
    max_bytes = settings.max_upload_mb * 1024 * 1024
    if len(content) > max_bytes:
        raise HTTPException(413, f"File exceeds {settings.max_upload_mb} MB limit.")
    if not content.startswith(b"%PDF"):
        raise HTTPException(400, "The uploaded file is not a valid PDF.")

    document_id = str(uuid4())
    stored = Path(settings.upload_dir) / f"{document_id}.pdf"
    stored.parent.mkdir(parents=True, exist_ok=True)
    stored.write_bytes(content)

    record = Document(
        id=document_id,
        filename=filename,
        stored_path=str(stored),
        status="processing",
    )
    db.add(record)
    db.commit()

    try:
        pages = extract_pdf(str(stored))
        chunks = chunk_pages(pages)
        if not chunks:
            raise ValueError("No extractable text was found in this PDF.")
        vector_store.add(chunks, document_id, filename)
        record.page_count = len(pages)
        record.chunk_count = len(chunks)
        record.status = "ready"
        db.commit()
    except Exception as exc:
        logger.exception("Document processing failed")
        record.status = "failed"
        record.error = str(exc)
        db.commit()
        if stored.exists():
            stored.unlink()
        raise HTTPException(500, "Document processing failed. Check server logs.")

    db.refresh(record)
    return record

@router.get("", response_model=list[DocumentOut])
def list_documents(db: Session = Depends(get_db)):
    return db.query(Document).order_by(Document.uploaded_at.desc()).all()

@router.get("/{document_id}", response_model=DocumentOut)
def get_document(document_id: str, db: Session = Depends(get_db)):
    record = db.get(Document, document_id)
    if not record:
        raise HTTPException(404, "Document not found.")
    return record

@router.delete("/{document_id}")
def delete_document(document_id: str, db: Session = Depends(get_db)):
    record = db.get(Document, document_id)
    if not record:
        raise HTTPException(404, "Document not found.")

    try:
        vector_store.remove_document(document_id)
    except Exception:
        logger.exception("Vector index rebuild failed during deletion")
        raise HTTPException(500, "Could not safely update the vector index.")

    path = Path(record.stored_path)
    if path.exists():
        path.unlink()

    db.delete(record)
    db.commit()
    return {"deleted": True, "id": document_id}
