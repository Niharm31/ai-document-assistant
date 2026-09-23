from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class DocumentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    filename: str
    page_count: int
    chunk_count: int
    status: str
    error: str | None = None
    uploaded_at: datetime

class Source(BaseModel):
    document: str
    page: int
    chunk: int
    score: float

class ChatRequest(BaseModel):
    question: str = Field(min_length=1, max_length=4000)
    document_id: str | None = None
    session_id: str = Field(default="default", min_length=1, max_length=64)

class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]
    session_id: str

class HistoryMessage(BaseModel):
    role: str
    content: str
    created_at: datetime
