import streamlit as st
import requests

st.set_page_config(page_title="AI Assistant", page_icon="🤖")

st.title("🤖 AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

document = st.text_area("Paste document (optional)")

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask anything...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    try:
        response = requests.post(
            "https://agentic-ai-backend-4kg7.onrender.com/agent",
            json={
                "question": user_input,
                "document": document
            }
        )

        if response.status_code == 200:

            result = response.json()["result"]

            if "answer" in result:
                answer = result["answer"]

            elif "summary" in result:
                answer = (
                    f"Summary:\n{result['summary']}\n\n"
                    f"Keywords:\n{', '.join(result['keywords'])}"
                )

            elif "document" in result:
                answer = (
                    f"Summary:\n{result['document']}\n\n"
                    f"Keywords:\n{', '.join(result['keywords'])}"
                )

            else:
                answer = "No response generated."

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

            with st.chat_message("assistant"):
                st.write(answer)

        else:
            st.error(f"Server Error: {response.status_code}")

    except Exception as e:
        st.error(f"Error: {str(e)}")