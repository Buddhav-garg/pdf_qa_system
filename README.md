
# 📄 PDF Q&A System (Local LLM Edition)

A Streamlit-powered app that allows users to upload large PDF files, index them using semantic embeddings, and ask natural language questions — powered entirely by **local models**.

No OpenAI or internet required!

---

## 🚀 Features

- 📤 Upload one or more PDFs
- ✂️ Intelligent chunking of large documents
- 🔍 Semantic search with Sentence Transformers + FAISS
- 🤖 Answer questions using a local LLM (TinyLlama 1.1B)
- 📚 Source traceability for each answer

---

## 🧰 Tech Stack

- Python 3.8+
- Streamlit
- SentenceTransformers
- FAISS (for vector search)
- llama-cpp-python (local LLM inference)
- PyMuPDF (PDF parsing)
- LangChain (text splitting)

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/pdf-qa-system.git
cd pdf-qa-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download TinyLlama GGUF model

Download this model file:

👉 [TinyLlama-1.1B-Chat-v1.0.Q4_0.gguf](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)

Place it in the `models/` directory:

```
pdf-qa-system/
├── models/
│   └── tinyllama-1.1b-chat-v1.0.Q4_0.gguf
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
pdf-qa-system/
├── app.py
├── chunker.py
├── embedder.py
├── pdf_handler.py
├── qa_engine.py
├── vector_store.py
├── requirements.txt
├── README.md
└── models/
    └── tinyllama-1.1b-chat-v1.0.Q4_0.gguf
```

---

## 💡 Notes

- Embedding model used: `all-MiniLM-L6-v2` from SentenceTransformers
- Vector similarity search: FAISS (L2 distance)
- Question answering LLM: TinyLlama 1.1B Chat, Q4 quantized
- You can swap in any GGUF model supported by `llama-cpp-python` (e.g., Mistral, Phi, LLaMA 2)

---

## 🙏 Acknowledgments

- [TinyLlama](https://huggingface.co/TinyLlama)
- [TheBloke](https://huggingface.co/TheBloke) for GGUF quantizations
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- [SentenceTransformers](https://www.sbert.net/)
