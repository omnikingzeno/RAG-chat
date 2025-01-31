# text_chunker.py
from unstructured.chunking.title import chunk_by_title
from unstructured.documents.elements import Element


def chunk_pdf_elements(elements):
    """Split elements into context-aware chunks using titles/headings"""
    chunks = chunk_by_title(
        elements=elements,
        max_characters=1500,  # Optimal for most LLMs
        combine_text_under_n_chars=200,
        new_after_n_chars=1200,
    )
    return [chunk.text for chunk in chunks]


if __name__ == "__main__":
    # Example usage for testing
    elements = [
        Element(),
        Element(),
        Element(),
    ]
    elements[0].text = "Title 1\nThis is the first section of the document."
    elements[0].category = "Title"
    elements[1].text = "This is the second section of the document."
    elements[1].category = "Paragraph"
    elements[2].text = "Title 2\nThis is the third section of the document."
    elements[2].category = "Title"

    chunks = chunk_pdf_elements(elements)
    for chunk in chunks:
        print(chunk)
