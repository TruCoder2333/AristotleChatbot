from src.text_split import split_into_chunks

def test_split_short_text():
    text = "Short text"
    chunks = split_into_chunks(text, chunk_size=1000, chunk_overlap=100)
    assert len(chunks) == 1
    assert chunks[0].page_content == text

def test_split_long_text():
    text = "A" * 3000  
    chunks = split_into_chunks(text, chunk_size=1000, chunk_overlap=100)
    assert len(chunks) >= 3 