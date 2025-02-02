import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils.embedder import generate_embeddings, embed_single_text

# Global variable for document cache
document_cache = []
embedding_cache = []


def retrieve_documents(query, documents=None):
    """Retrieves the most relevant documents for a given query."""
    global document_cache, embedding_cache

    # Load documents if not provided or not cached
    if documents is None:
        from data.loaders import load_documents

        documents = load_documents()

    if not documents:
        return []

    if not document_cache:  # Cache documents if not already done
        document_cache = documents
        # Generate and cache embeddings for documents
        embedding_cache = generate_embeddings(document_cache)

    # Generate embedding for query
    query_embedding = embed_single_text(query)

    # Reshape embeddings for cosine similarity
    query_embedding = np.array(query_embedding).reshape(1, -1)
    doc_embeddings = np.array(embedding_cache)

    # Compute similarity scores
    scores = cosine_similarity(query_embedding, doc_embeddings)
    ranked_docs = sorted(zip(scores[0], document_cache), reverse=True)

    # Return top 3 documents
    return [doc for score, doc in ranked_docs[:3]]
