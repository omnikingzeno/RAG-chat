import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.jina.ai/v1/embeddings"
API_KEY = os.getenv("JINA_API_KEY")


def generate_embeddings(texts):
    """
    Generate embeddings for a list of texts using Jina AI API

    Parameters:
    texts (list): A list of docs to generate embeddings for

    Returns:
    list of list of float: List of embeddings for each document
    """

    headers = {"Content-type": "application/json", "Authorization": f"Bearer {API_KEY}"}

    data = {
        "model": "jina-clip-v2",
        "dimensions": 1024,
        "normalized": True,
        "embedding_type": "float",
        "input": [{"text": text} for text in texts],
    }

    response = requests.post(API_URL, headers=headers, json=data)

    response_data = response.json()

    if response.status_code != 200:
        raise Exception(f"Failed to generate embeddings: {response_data}")

    return [item["embedding"] for item in response_data["data"]]


def embed_single_text(text):
    """ "
    Generate embeddings for a single text using Jina AI API

    Parameters:
    text (str): A single user prompt to generate embeddings for

    Returns:
    list of float: Embeddings for the text
    """

    return generate_embeddings([text])[0]
