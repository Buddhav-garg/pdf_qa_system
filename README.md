# PDF Q&A System

A Streamlit-powered web app that allows users to upload large PDFs, index them, and ask questions using a local embedding model and OpenAI's GPT API.

## 🚀 Features
- Upload one or more PDFs
- Intelligent text chunking
- Vector embedding using SentenceTransformers
- Search and match with FAISS
- Query response via GPT-3.5 with source traceability

## 🧰 Tech Stack
- Python 3.8+
- Streamlit
- SentenceTransformers
- FAISS
- PyMuPDF
- OpenAI GPT
- LangChain (for text splitting)

## 🛠️ Setup Instructions

```bash
# Clone the repo
$ git clone https://github.com/your-username/pdf-qa-system.git
$ cd pdf-qa-system

# Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
$ pip install -r requirements.txt

# Set your OpenAI key
$ export OPENAI_API_KEY="your-api-key"

# Run the app
$ streamlit run app.py
```

## 📁 Project Structure
See directory structure in source tree.

## 🧠 Notes
- Chunking is done via LangChain's `RecursiveCharacterTextSplitter`.
- Uses `all-MiniLM-L6-v2` for fast, efficient embeddings.
- You can replace OpenAI with a local LLM like `llama.cpp` for a fully local pipeline.
