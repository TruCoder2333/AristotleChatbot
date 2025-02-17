from src.vectorstore import build_faiss_index
from src.embeddings import get_embedding_model
from langchain.docstore.document import Document

def test_build_faiss_index():
    docs = [
        Document(page_content="Hello World", metadata={"id": 1}),
        Document(page_content="Foo Bar", metadata={"id": 2}),
    ]
    embedding_model = get_embedding_model()
    index = build_faiss_index(docs, embedding_model)
    assert index is not None

def test_similarity_search():
    docs = [
        Document(page_content="The cat sat on the mat", metadata={"id": "cat"}),
        Document(page_content="A dog ate a bone", metadata={"id": "dog"})
    ]
    embedding_model = get_embedding_model()
    index = build_faiss_index(docs, embedding_model)

    results = index.similarity_search("cat", k=1)
    top_doc = results[0]
    assert "cat" in top_doc.page_content.lower()