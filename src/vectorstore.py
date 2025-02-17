from langchain_community.vectorstores import FAISS

def build_faiss_index(chunks, embedding_model):
    return FAISS.from_documents(chunks, embedding_model)