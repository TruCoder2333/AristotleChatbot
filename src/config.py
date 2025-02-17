import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

CHAT_MODEL_NAME = "gpt-3.5-turbo-16k"

EMBEDDING_MODEL_NAME = "text-embedding-3-small"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

TOP_K = 3
BASE_DIR = os.getenv("BASE_DIR", "")
RAW_DATA_DIR = os.path.join(BASE_DIR, "data/raw")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data/processed")
VECTOR_INDEX_DIR = "data\vector_store"

TEMPERATURE = 0.0
MAX_TOKENS = 1500