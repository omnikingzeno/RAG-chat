import streamlit as st
import requests

API_URL = "http://localhost:5000/api/chat"
SESSION_ID = "streamlit-session"

st.title("RAG-Chat Bot Frontend")

# Initialize conversation messages in session state if not already set
if "messages" not in st.session_state:
    st.session_state.messages = (
        []
    )  # Each entry: {"role": "user" or "assistant", "content": "message text"}


# Define a function to call the chat API
def get_chat_response(query):
    payload = {"message": query, "session_id": SESSION_ID}
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data.get("response", "No response received.")
        else:
            return f"Error: {response.json().get('error', 'Unknown error')}"
    except Exception as e:
        return f"Request failed: {e}"


# Display conversation history using Streamlit's chat message containers
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Use st.chat_input to get new user input; it submits on Enter key
if user_input := st.chat_input("Type your message"):
    # Append and display the user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Display a temporary assistant message (with a spinner) so the user knows that a response is loading
    with st.chat_message("assistant"):
        st.markdown("Typing...")

    # Get the assistant response from the API
    response = get_chat_response(user_input)

    # Append the assistant response to conversation history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Rerun the app to update the chat interface, now showing the new assistant message
    st.rerun()
