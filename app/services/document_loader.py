from pathlib import Path
import fitz

def extract_pdf(path: str) -> list[dict]:
    pages = []
    with fitz.open(path) as pdf:
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text("text").strip()
            if text:
                pages.append({"page": page_number, "text": text})
    return pages
