import json
from pathlib import Path
import faiss
import numpy as np
from app.core.config import settings
from app.services.embeddings import embed_texts, embed_query

class VectorStore:
    def __init__(self):
        self.directory = Path(settings.vector_dir)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.index_path = self.directory / "index.faiss"
        self.meta_path = self.directory / "metadata.json"
        self.index = None
        self.metadata = []
        self._load()

    def _load(self):
        if self.index_path.exists() and self.meta_path.exists():
            self.index = faiss.read_index(str(self.index_path))
            self.metadata = json.loads(self.meta_path.read_text(encoding="utf-8"))

    def _save(self):
        if self.index is None or not self.metadata:
            if self.index_path.exists():
                self.index_path.unlink()
            if self.meta_path.exists():
                self.meta_path.unlink()
            return
        faiss.write_index(self.index, str(self.index_path))
        self.meta_path.write_text(
            json.dumps(self.metadata, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def add(self, chunks, document_id: str, filename: str):
        vectors = np.asarray(
            embed_texts([c.text for c in chunks]), dtype="float32"
        )
        if self.index is None:
            self.index = faiss.IndexFlatIP(vectors.shape[1])
        start = len(self.metadata)
        self.index.add(vectors)
        for offset, chunk in enumerate(chunks):
            self.metadata.append({
                "document_id": document_id,
                "document": filename,
                "page": chunk.page,
                "chunk": chunk.chunk_index,
                "text": chunk.text,
                "vector_id": start + offset,
            })
        self._save()

    def remove_document(self, document_id: str) -> int:
        """Remove a document and rebuild the FAISS index from remaining chunks.

        Rebuilding is intentionally used here because IndexFlatIP does not
        provide safe arbitrary deletion while keeping metadata IDs aligned.
        """
        remaining = [m for m in self.metadata if m["document_id"] != document_id]
        removed = len(self.metadata) - len(remaining)
        if removed == 0:
            return 0

        if not remaining:
            self.index = None
            self.metadata = []
            self._save()
            return removed

        vectors = np.asarray(
            embed_texts([m["text"] for m in remaining]), dtype="float32"
        )
        self.index = faiss.IndexFlatIP(vectors.shape[1])
        self.index.add(vectors)

        for idx, item in enumerate(remaining):
            item["vector_id"] = idx

        self.metadata = remaining
        self._save()
        return removed

    def search(self, query: str, document_id: str | None = None, top_k: int = 5):
        if self.index is None or not self.metadata:
            return []

        q = np.asarray(embed_query(query), dtype="float32")
        candidate_k = min(max(top_k * 8, top_k), self.index.ntotal)
        scores, ids = self.index.search(q, candidate_k)

        results = []
        for score, idx in zip(scores[0], ids[0]):
            if idx < 0:
                continue
            item = self.metadata[int(idx)]
            if document_id and item["document_id"] != document_id:
                continue
            results.append({**item, "score": float(score)})
            if len(results) >= top_k:
                break
        return results

vector_store = VectorStore()
