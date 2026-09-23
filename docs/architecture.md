# Architecture

The application follows a small service-oriented architecture.

```text
PDF
 |
 v
PyMuPDF
 |
 v
Page-aware chunks
 |
 v
Sentence Transformers
 |
 v
FAISS
 |
 v
Retriever
 |
 +----> Context
          |
          v
    OpenAI-compatible LLM
          |
          v
 Answer + Sources
```

The vector store keeps document metadata alongside each vector so retrieved
chunks can be mapped back to their original filename and page.
