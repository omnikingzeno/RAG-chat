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
#     pdf_path = "table.pdf"
#     elements = extract_pdf_elements(pdf_path)
#     for element in elements:
#         print(element)
