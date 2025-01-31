from unstructured.partition.pdf import partition_pdf


def extract_text_with_unstructured(pdf_path):
    elements = partition_pdf(pdf_path, strategy="auto")
    text = "\n".join([elem.text for elem in elements])
    return text


# if __name__ == "__main__":
#     print(extract_text_with_unstructured("path_to_pdf.pdf"))
