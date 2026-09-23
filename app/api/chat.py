from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.config import settings
from app.database.database import get_db
from app.database.models import ChatMessage, Document
from app.models.document import ChatRequest, ChatResponse, HistoryMessage, Source
from app.services.llm import generate_answer
from app.services.vector_store import vector_store

router = APIRouter(prefix="/api/chat", tags=["chat"])

@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    if request.document_id and not db.get(Document, request.document_id):
        raise HTTPException(404, "Document not found.")

    previous = (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == request.session_id)
        .order_by(ChatMessage.created_at.desc())
        .limit(10)
        .all()
    )
    previous = list(reversed(previous))

    results = vector_store.search(
        request.question,
        request.document_id,
        settings.top_k,
    )

    answer = generate_answer(
        request.question,
        results,
        history=[{"role": m.role, "content": m.content} for m in previous],
    )

    db.add(ChatMessage(
        session_id=request.session_id,
        role="user",
        content=request.question,
    ))
    db.add(ChatMessage(
        session_id=request.session_id,
        role="assistant",
        content=answer,
    ))
    db.commit()

    sources = [
        Source(
            document=r["document"],
            page=r["page"],
            chunk=r["chunk"],
            score=round(r["score"], 4),
        )
        for r in results
    ]
    return ChatResponse(
        answer=answer,
        sources=sources,
        session_id=request.session_id,
    )

@router.get("/{session_id}/history", response_model=list[HistoryMessage])
def history(session_id: str, db: Session = Depends(get_db)):
    return (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.asc())
        .all()
    )

@router.delete("/{session_id}/history")
def clear_history(session_id: str, db: Session = Depends(get_db)):
    db.query(ChatMessage).filter(ChatMessage.session_id == session_id).delete()
    db.commit()
    return {"cleared": True, "session_id": session_id}
