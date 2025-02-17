import os
import argparse
from src.config import *
from src.text_split import load_raw_texts, split_into_chunks
from src.embeddings import get_embedding_model
from src.vectorstore import build_faiss_index
from src.retriever import get_retriever
from src.rag_chain import create_rag_chain

def main(query: str):
    raw_texts = load_raw_texts(PROCESSED_DATA_DIR)

    all_docs = []
    for text in raw_texts:
        docs = split_into_chunks(text)
        all_docs.extend(docs)


    embedding_model = get_embedding_model()
    vector_store = build_faiss_index(all_docs, embedding_model)

    retriever = get_retriever(vector_store)

    rag_chain = create_rag_chain(retriver=retriever)

    response = rag_chain.invoke(query)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run RAG-based chatbot.")
    parser.add_argument("query", type=str, help="User's input question")
    args = parser.parse_args()
    
    main(args.query)