from app.services.chunker import chunk_pages

def test_chunker_preserves_pages():
    chunks = chunk_pages([{"page": 3, "text": "hello " * 400}], size=100, overlap=10)
    assert chunks
    assert all(c.page == 3 for c in chunks)

def test_invalid_overlap():
    try:
        chunk_pages([{"page": 1, "text": "hello"}], size=10, overlap=10)
    except ValueError:
        return
    assert False

def test_chunk_indexes_are_sequential():
    chunks = chunk_pages([{"page": 1, "text": "abc " * 200}], size=40, overlap=5)
    assert [c.chunk_index for c in chunks] == list(range(len(chunks)))
