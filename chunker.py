from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text, source_name="Unknown"):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(text)
    return [{"text": chunk, "source": source_name} for chunk in chunks]
