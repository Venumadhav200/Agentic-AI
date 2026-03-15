import streamlit as st
import requests

st.title("🌍 AI Multi-Agent Assistant")

st.write("Ask questions, summarize documents, or search the internet.")

# User document input
document = st.text_area("Paste your document (optional)")

# User question
question = st.text_input("Ask a question")

task = st.selectbox(
    "Select task",
    ["summarize", "question", "search"]
)

if st.button("Submit"):

    url = "http://127.0.0.1:8000/agent"

    payload = {
        "task": task,
        "document": document,
        "question": question
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()
        st.subheader("Response")
        st.write(result["result"])
    else:
        st.error("API request failed")