from .config import TOP_K

def get_retriever(faiss_index, k: int=None):
    if k is None:
        k = TOP_K
    return faiss_index.as_retriever(search_kwargs={"k": k})