import os
from .config import CHUNK_SIZE, CHUNK_OVERLAP
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_raw_texts(data_dir):
    texts = []
    for file in os.listdir(data_dir):
        if file.endswith("txt"):
            with open(os.path.join(data_dir, file), "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts

def split_into_chunks(text: str, chunk_size: int = None, chunk_overlap: int=None):
    if chunk_size is None:
        chunk_size = CHUNK_SIZE
    if chunk_overlap is None:
        chunk_overlap = CHUNK_OVERLAP
        
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    docs = splitter.create_documents([text])
    return docs