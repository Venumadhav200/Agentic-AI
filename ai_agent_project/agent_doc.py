from groq import Groq
from dotenv import load_dotenv
import os
import re

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def summarize_and_extract(document):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Summarize the document in 2-3 sentences."
            },
            {
                "role": "user",
                "content": document
            }
        ],
        temperature=0.3,
        max_tokens=200
    )

    summary = response.choices[0].message.content

    words = re.findall(
        r'\b[a-zA-Z]{4,}\b',
        document.lower()
    )

    keywords = []

    for w in words:
        if w not in keywords:
            keywords.append(w)

        if len(keywords) == 5:
            break

    return {
        "document": summary,
        "keywords": keywords
    }