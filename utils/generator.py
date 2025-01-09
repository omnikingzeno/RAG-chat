def generate_response(query, documents):
    """
    Generate a response based in query and the retrieved documents.

    Args :
        query (str) : User's input query.
        documents (list) : List of retrieved documents.

        Returns :
            str : Generated response combining query contxt and document.
    """
    if not documents:
        return f"Sorry, I could not find any documents related to your query: {query}"

    # Generate a reponse by concatenating the top documents
    response = f"For your query : '{query}', here is what I found :\n\n"
    for i, doc in enumerate(documents, 1):
        response += f"Document {i} : \n {doc} \n\n"

    return response.strip()
