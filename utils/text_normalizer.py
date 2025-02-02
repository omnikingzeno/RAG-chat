# text_normalizer.py
from unstructured.documents.elements import Element
from unstructured.cleaners.core import (
    replace_unicode_quotes,
    clean_non_ascii_chars,
)


def normalize_pdf_elements(elements):
    """Normalize text casing and encoding in each element"""
    normalized_elements = []

    for elem in elements:
        text = elem.text

        # Normalization operations
        text = text.lower()  # Key for embedding consistency
        text = clean_non_ascii_chars(text)
        text = replace_unicode_quotes(text).strip()

        # Preserve element type and metadata
        normalized_elem = Element()
        normalized_elem.text = text
        normalized_elem.metadata = elem.metadata
        normalized_elem.category = elem.category
        normalized_elements.append(normalized_elem)

    return normalized_elements


# if __name__ == "__main__":
#     # Example usage for testing
#     elements = [
#         Element(),
#         Element(),
#         Element(),
#     ]
#     elements[0].text = "Header TEXT"
#     elements[0].category = "Header"
#     elements[1].text = "This is a SAMPLE text."
#     elements[1].category = "Paragraph"
#     elements[2].text = "Footer TEXT"
#     elements[2].category = "Footer"

#     normalized_elements = normalize_pdf_elements(elements)
#     for element in normalized_elements:
#         print(element.text)
