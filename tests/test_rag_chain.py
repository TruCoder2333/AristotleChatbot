from langchain.llms.base import BaseLanguageModel
from langchain.schema import BaseRetriever, Document, AIMessage, LLMResult, Generation
from src.rag_chain import create_rag_chain

class DummyRetriever(BaseRetriever):
    def _get_relevant_documents(self, query: str):
        return [Document(page_content="Document context about cats", metadata={})]

def test_basic_rag_chain(mocker):
    retriever = DummyRetriever()  
    mock_llm = mocker.Mock(spec=BaseLanguageModel)
    
    mock_llm.generate_prompt.return_value = LLMResult(
        generations=[[Generation(text="Cats are great pets.")]]
    )

    chain = create_rag_chain(retriever)
    chain.combine_documents_chain.llm_chain.llm = mock_llm

    response = chain.invoke("Tell me about cats")
    assert "Cats are great pets" in response["result"]
    mock_llm.generate_prompt.assert_called()