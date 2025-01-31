from unstructured.documents.elements import Element
from unstructured.cleaners.core import (
    clean_non_ascii_chars,
    clean_extra_whitespace,
    replace_unicode_quotes,
    remove_punctuation,
)


def clean_pdf_elements(elements):
    """Filter headers/footers and clean text in each element"""
    cleaned_elements = []

    # Filter out headers/footers using metadata
    for elem in elements:
        if elem.category in ("Header", "Footer"):
            continue

        # Clean text while preserving element type
        text = elem.text
        text = clean_non_ascii_chars(text)
        text = clean_extra_whitespace(text)
        text = replace_unicode_quotes(text)
        text = remove_punctuation(text)  # Optional

        # Create new element with cleaned text and original metadata
        cleaned_elem = Element()
        cleaned_elem.text = text
        cleaned_elem.metadata = elem.metadata
        cleaned_elem.category = elem.category
        cleaned_elements.append(cleaned_elem)

    return cleaned_elements


if __name__ == "__main__":
    # Example usage for testing
    elements = [
        Element(),
        Element(),
        Element(),
    ]
    elements[0].text = "Header text"
    elements[0].category = "Header"
    elements[1].text = "This is a sample          text."
    elements[1].category = "Paragraph"
    elements[2].text = "Footer text"
    elements[2].category = "Footer"

    cleaned_elements = clean_pdf_elements(elements)
    for element in cleaned_elements:
        print(element.text)
