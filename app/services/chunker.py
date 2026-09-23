from dataclasses import dataclass

@dataclass
class Chunk:
    text: str
    page: int
    chunk_index: int

def chunk_pages(pages: list[dict], size: int = 900, overlap: int = 120) -> list[Chunk]:
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")
    chunks: list[Chunk] = []
    index = 0
    for item in pages:
        text = " ".join(item["text"].split())
        start = 0
        while start < len(text):
            end = min(start + size, len(text))
            piece = text[start:end].strip()
            if piece:
                chunks.append(Chunk(piece, item["page"], index))
                index += 1
            if end >= len(text):
                break
            start = end - overlap
    return chunks
