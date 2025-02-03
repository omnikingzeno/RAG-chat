import streamlit as st
import requests

API_URL = "http://localhost:5000/api/chat"
SESSION_ID = "streamlit-session"

st.title("RAG-Chat Bot Frontend")

# Initialize conversation history in session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []  # Each entry: {"query": ..., "response": ...}


# Define a function to send the query
def send_query(query):
    if not query:
        st.error("Please enter a query.")
        return
    payload = {"message": query, "session_id": SESSION_ID}
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            data = response.json()
            answer = data.get("response", "No response received.")
            # Append current query and response to the conversation history
            st.session_state.conversation.append({"query": query, "response": answer})
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"Request failed: {e}")


# Display conversation history at the top of the page
st.markdown("## Conversation History")
for chat in st.session_state.conversation:
    st.markdown(f"**You:** {chat['query']}")
    st.markdown(f"**Chatbot:** {chat['response']}")
    st.markdown("---")

# Use a form at the bottom for entering a new query,
# which supports pressing Enter (Return) to submit
with st.form(key="chat_form", clear_on_submit=True):
    query = st.text_input("Enter your query:")
    submitted = st.form_submit_button("Send")
    if submitted:
        send_query(query)
