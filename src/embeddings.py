from .config import EMBEDDING_MODEL_NAME
from langchain_openai.embeddings import OpenAIEmbeddings

def get_embedding_model():
    embeddings = OpenAIEmbeddings(
        model=EMBEDDING_MODEL_NAME
    )
    return embeddings