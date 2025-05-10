import streamlit as st
from pdf_handler import parse_pdf
from chunker import chunk_text
from embedder import embed_chunks, load_embedder
from vector_store import create_or_update_index, query_index
from qa_engine import answer_query

st.title("📄 PDF Q&A System")

uploaded_files = st.file_uploader("Upload one or more PDF files", type="pdf", accept_multiple_files=True)
query = st.text_input("Ask a question about the uploaded documents")

if uploaded_files:
    raw_texts = []
    for file in uploaded_files:
        text = parse_pdf(file)
        chunks = chunk_text(text, source_name=file.name)
        raw_texts.extend(chunks)

    model = load_embedder()
    docs_with_embeddings = embed_chunks(raw_texts, model)
    create_or_update_index(docs_with_embeddings)
    st.success("PDFs processed and indexed.")

    if query:
        results = query_index(query, model)
        answer = answer_query(query, results)
        st.subheader("Answer")
        st.write(answer)
        st.markdown("---")
        st.subheader("Sources")
        for r in results:
            st.markdown(f"- {r['source']}")
