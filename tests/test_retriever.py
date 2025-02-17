from src.vectorstore import build_faiss_index
from src.retriever import get_retriever
from src.embeddings import get_embedding_model
from langchain.docstore.document import Document

def test_retrieve():
    docs = [
        Document(page_content="Apple orchard", metadata={"id": 1}),
        Document(page_content="Banana plantation", metadata={"id": 2})
    ]
    embedding_model = get_embedding_model()
    index = build_faiss_index(docs, embedding_model)
    retriever = get_retriever(index, k=1)

    results = retriever.get_relevant_documents("apple")
    assert len(results) == 1
    assert "Apple orchard".lower() in results[0].page_content.lower()
