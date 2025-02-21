from unstructured.partition.pdf import partition_pdf


def extract_pdf_elements(pdf_path):
    """
    Extract elements (titles, paragraphs, etc.) with metadata from PDF

    Parameters:
    pdf_path: Path to the PDF file

    Returns:
    List of extracted elements with metadata
    """
    return partition_pdf(
        filename=pdf_path,
        strategy="auto",
        infer_table_structure=False,
        include_page_headers=False,
    )


# if __name__ == "__main__":
#     # Example usage for testing
#     pdf_path = "Review of Endodontics and Operative Dentistry by Garg, Nisha.pdf"
#     elements = extract_pdf_elements(pdf_path)
#     # for element in elements:
#     #     print(element)
#     # Write the extracted text from each element to a file.
#     with open("extracted_text.txt", "w", encoding="utf-8") as f:
#         for element in elements:
#             # Assuming each element has a 'text' attribute.
#             f.write(element.text + "\n")
