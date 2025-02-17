from .config import CHAT_MODEL_NAME, TEMPERATURE
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_openai import ChatOpenAI

def create_rag_chain(retriver):
    llm = ChatOpenAI(model_name=CHAT_MODEL_NAME, temperature=TEMPERATURE)

    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriver,
        return_source_documents=True
    )
    return rag_chain