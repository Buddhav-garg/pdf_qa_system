from sentence_transformers import SentenceTransformer

def load_embedder():
    return SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks, model):
    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts)
    return [{"embedding": emb, "text": chunks[i]["text"], "source": chunks[i]["source"]} for i, emb in enumerate(embeddings)]
