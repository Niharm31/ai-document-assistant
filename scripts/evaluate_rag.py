"""Evaluate retrieval against a small, user-supplied labeled dataset.

Usage:
    python scripts/evaluate_rag.py

The script reports Hit@K and MRR. It does not invent or claim benchmark
results; the input dataset must contain the expected document/page labels.
"""
import json
from pathlib import Path
from app.core.config import settings
from app.services.vector_store import vector_store

def main():
    path = Path("evals/sample_questions.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = [
        q for q in data.get("questions", [])
        if not q["question"].startswith("REPLACE_WITH_")
    ]
    if not rows:
        print("No labeled evaluation questions found.")
        print("Edit evals/sample_questions.json with real questions and expected pages.")
        return

    hits = 0
    reciprocal_ranks = []

    for item in rows:
        results = vector_store.search(
            item["question"],
            item.get("document_id"),
            settings.top_k,
        )
        expected = set(item.get("expected_pages", []))
        rank = None

        for i, result in enumerate(results, start=1):
            if result["page"] in expected:
                rank = i
                break

        if rank:
            hits += 1
            reciprocal_ranks.append(1 / rank)
        else:
            reciprocal_ranks.append(0)

    total = len(rows)
    print(f"Questions: {total}")
    print(f"Hit@{settings.top_k}: {hits / total:.3f}")
    print(f"MRR@{settings.top_k}: {sum(reciprocal_ranks) / total:.3f}")

if __name__ == "__main__":
    main()
