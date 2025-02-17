import numpy as np
from src.embeddings import get_embedding_model

def test_single_embedding():
    embedding_model = get_embedding_model()
    vector = embedding_model.embed_query("Hello world")
    assert isinstance(vector, list)
    assert len(vector) == 1536 

def test_multiple_embeddings():
    embedding_model = get_embedding_model()
    vectors = embedding_model.embed_documents(["Hello", "World"])
    assert len(vectors) == 2
    assert all(len(vec) == 1536 for vec in vectors) 