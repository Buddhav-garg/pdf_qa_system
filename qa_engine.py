from llama_cpp import Llama

llm = Llama(model_path="C:/Users/buddh/Downloads/pdf_qa_system/pdf_qa_system/models/tinyllama-1.1b-chat-v1.0.Q4_0.gguf", n_ctx=1024)

def answer_query(question, chunks):
    context = "\n\n".join([chunk["text"] for chunk in chunks])
    prompt = f"[INST] Answer the question using the context below. \n\nContext:\n{context}\n\nQuestion: {question} [/INST]"

    output = llm(prompt, max_tokens=300, stop=["</s>"])
    return output["choices"][0]["text"].strip()
