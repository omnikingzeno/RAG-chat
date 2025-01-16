from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Global variables for vectorizer and document cache
tfidf_vectorizer = TfidfVectorizer()
document_cache = []


def retrieve_documents(query, documents=None):
    """Retrieves the most relevant documents for a given query."""
    global document_cache

    # Load documents if not provided or not cached
    if documents is None:
        from data.loaders import load_documents

        documents = load_documents()

    if not documents:
        return []

    if not document_cache:  # Cache documents if not already done
        document_cache = documents

    # Vectorize documents and query
    doc_vectors = tfidf_vectorizer.fit_transform(document_cache)
    query_vector = tfidf_vectorizer.transform([query])

    # Compute similarity scores
    scores = cosine_similarity(query_vector, doc_vectors)
    ranked_docs = sorted(zip(scores[0], document_cache), reverse=True)

    # Return top 3 documents
    return [doc for score, doc in ranked_docs[:3]]


# Testing the retriever
# import sys
# import os

# if __name__ == "__main__":
#     # Add the parent directory to the sys.path
#     sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#     # print(sys.path)

#     from data.loaders import load_documents

#     docs = load_documents()
#     query = "Friends"
#     results = retrieve_documents(query, docs)
#     print("Top documents for you query:")
#     for result in results:
#         print(result[:30])
