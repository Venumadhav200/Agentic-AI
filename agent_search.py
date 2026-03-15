import wikipedia
import re
from transformers import pipeline

# small summarization model
generator = pipeline("text-generation", model="gpt2")


def clean_query(query):
    query = query.lower()

    remove_words = [
        "what is",
        "define",
        "explain",
        "tell me about",
        "give me",
        "information about"
    ]

    for word in remove_words:
        query = query.replace(word, "")

    return query.strip()


def search_internet(query):

    try:

        cleaned = clean_query(query)

        results = wikipedia.search(cleaned)

        if not results:
            return {"answer": "Sorry, I couldn't find information for this query."}

        try:
            page = wikipedia.page(results[0], auto_suggest=False)
        except wikipedia.DisambiguationError as e:
            page = wikipedia.page(e.options[0])

        text = page.summary[:1200]

        prompt = f"""
Explain this topic in simple words.

Topic: {query}

Information:
{text}

Answer:
"""

        result = generator(prompt, max_new_tokens=80)[0]["generated_text"]

        answer = result.replace(prompt, "").strip()

        return {"answer": answer}

    except Exception:
        return {"answer": "Sorry, I couldn't find information for this query."}