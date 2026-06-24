from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def search_internet(query):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
                You are a helpful AI assistant.

                Give accurate and concise answers.
                """
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=0.3,
        max_tokens=800
    )

    return {
        "answer": response.choices[0].message.content
    }