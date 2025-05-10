import faiss
import numpy as np

index = None
stored_chunks = []

def create_or_update_index(docs):
    global index, stored_chunks
    vectors = np.array([d["embedding"] for d in docs]).astype("float32")
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    stored_chunks = docs

def query_index(query, model, k=5):
    q_emb = np.array([model.encode(query)]).astype("float32")
    D, I = index.search(q_emb, k)
    return [stored_chunks[i] for i in I[0]]
