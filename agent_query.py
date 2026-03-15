from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def answer_query(document, question):

    prompt = f"""
Answer the question using the document.

Document:
{document}

Question:
{question}

Answer:
"""

    result = generator(prompt, max_new_tokens=50)[0]["generated_text"]

    return {
        "answer": result
    }