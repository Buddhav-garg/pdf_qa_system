import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def answer_query(question, chunks):
    context = "\n\n".join([chunk["text"] for chunk in chunks])
    prompt = f"Answer the question using the context below.\n\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer:"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
