import re
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter 


def clean_text(text: str):
    """Clean text by removing special characters, spaces, latex-style equations, and multiple newlines.
    Args:
        text (str): The text to clean.
    Returns:
        str: The cleaned text."""

    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"\$\$.*?\$\$", "", text)
    text = re.sub(r"\$.*?\$", "", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text


def split_text(
    file_content: str, chunk_size: int = 1000, chunk_overlap: int = 300
) -> List[str]:
    """Split text into chunks of size chunk_size. Each chunk is separated by two newlines.
    Args:
        file_content (str): The text to split.
        chunk_size (int): The size of each chunk.
    Returns:
        List[str]: The list of text chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )

    splitted_text = []
    for i in text_splitter.create_documents([file_content]):
        splitted_text.append(i.page_content)
    return splitted_text