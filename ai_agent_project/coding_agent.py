from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def coding_agent(query):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
                You are an expert coding assistant.

                Help with:
                - Python
                - C++
                - Java
                - DSA
                - LeetCode
                - Debugging
                - SQL

                Give clean and correct code.
                """
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=0.2,
        max_tokens=800
    )

    return {
        "answer": response.choices[0].message.content
    }