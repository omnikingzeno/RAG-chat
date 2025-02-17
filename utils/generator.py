import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://codestral.mistral.ai/v1/chat/completions"
API_KEY = os.getenv("API_KEY")


def generate_response(query, documents, conversation_history=None):
    """
    Generate a response using the Codestral LLM API.

    Args :
        query (str) : User's input query.
        documents (list) : List of retrieved documents.
        conversation_history (list) : list of conversation messages

        Returns :
            str : Generated response from the LLM.
    """

    # construct context from documents
    context = "\n\n".join(
        [f"Document {i} : \n {doc} \n\n" for i, doc in enumerate(documents, 1)]
    )

    # Build the messages list
    messages = [
        {
            "role": "system",
            "content": """You are a helpful assistant, which answers user queries in a truthful manner.
            If you find the given context any useful to answer the question, otherwise if you already know the answer, you can directly answer the question.
            However if a context contains the answer, YOU MUST USE IT.
            If no answer found from the given context, you can generate the answer from your own knowledge but add a Note at the end of the answer stating that 'No answer found in the context'.
            e.g. of the question that will be asked by user along with context, however the context can be empty as well, so respond accordingly.
            <User query>
            Context: <Context>""",
        }
    ]
    if conversation_history:

        messages.extend(conversation_history)
    messages.append({"role": "user", "content": f"{query}\n\nContext:\n{context}"})

    # print(messages)

    # API request payload
    payload = {"model": "codestral-latest", "messages": messages}

    # API request header
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Extract the response content
        assistant_reply = response.json()["choices"][0]["message"]["content"]
        return assistant_reply.strip()

    except Exception as e:
        return f"Error generating response: {e}"
