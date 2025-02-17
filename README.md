🤖 Aristotle Chatbot

A Retrieval-Augmented Generation (RAG)-powered chatbot that specializes in Aristotle’s philosophy. Built with GPT API, LangChain, FAISS, and vector databases, this chatbot can answer questions based on Aristotle's works (poetics, politics, ethics) and provide philosophical insights with more detail and nuance than base GPT

📌 Features

🚀 Quick Start

1️⃣ Clone the Repository

git clone https://github.com/yourusername/aristotle-chatbot.git
cd aristotle-chatbot

2️⃣ Set Up a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here

5️⃣ Run the Chatbot

python src/main.py "What is Aristotle's view on virtue?"

🛠 Project Structure

├── src/                      # Core source code
│   ├── main.py               # Entry point for the chatbot
│   ├── config.py             # Configuration settings
│   ├── text_split.py      # Splits Aristotle's texts into chunks
│   ├── embeddings.py         # Generates embeddings using OpenAI
│   ├── vectorstore.py        # Handles FAISS vector indexing
│   ├── retriever.py          # Retrieves relevant text from vector DB
│   ├── rag_chain.py          # Constructs RAG pipeline
│   ├── __init__.py           # Package initializer
├── tests/                    # Unit and integration tests
│   ├── test_text_split.py    
│   ├── test_embeddings.py    
│   ├── test_vectorstore.py
│   ├── test_retriever.py       
│   ├── test_rag_chain.py     
├── data/                     # Stores raw & processed text
│   ├── raw/                  # Raw Aristotle texts
│   ├── processed/            # Chunked texts for embedding
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation

🏛 How It Works

1️⃣ Text Processing & Chunking

Aristotle’s texts are split into smaller chunks.

Overlapping chunks help preserve context.

2️⃣ Embedding Generation

Uses OpenAI’s text-embedding-ada-002 model to convert text into vector representations.

3️⃣ Vector Database (FAISS/Chroma)

Chunks are stored in a vector database for fast similarity search.

4️⃣ Retrieval & Augmented Response

The chatbot retrieves the most relevant text chunks.

The LLM (GPT-3.5/4) then generates an answer using the retrieved context.

🔍 Example Query

python src/main.py "What is Aristotle's concept of Eudaimonia?"

📝 Example Output:

Eudaimonia, according to Aristotle, refers to "flourishing" or "the highest human good." In his Nicomachean Ethics, he argues that eudaimonia is achieved through virtuous living and rational activity in accordance with one's nature.

🔧 Configuration

Modify config.py to change:

Chunk size & overlap for text splitting.

Embedding model used.

Number of results (TOP_K) retrieved from the vector store.

📚 Expanding the Knowledge Base

To add more Aristotle texts:

Place the new text file in data/raw/.

Run:

python scripts/preprocess_data.py
python scripts/rebuild_vector_db.py

The chatbot will now include the new text in retrieval!

🛠 Testing

Run tests using pytest:

pytest tests/

To avoid real API calls, tests mock OpenAI’s responses with pytest-mock.

⚡ Future Improvements

✅ Support for more classical texts.

✅ Fine-tuned Aristotle-specific LLM.

✅ Web-based interface for interactive querying.

⚖️ License

MIT License. See LICENSE for details.
