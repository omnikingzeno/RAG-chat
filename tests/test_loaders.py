import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.loaders import load_documents


class TestLoaders(unittest.TestCase):
    def test_load_documents_empty(self):
        folder_path = "tests/test_documents_empty"
        os.makedirs(folder_path, exist_ok=True)
        documents = load_documents(folder_path)
        self.assertEqual(
            len(documents), 0, "Should return an empty list for empty folder"
        )

    def test_load_documents_with_files(self):
        folder_path = "tests/test_documents_with_files"
        os.makedirs(folder_path, exist_ok=True)
        with open(f"{folder_path}/doc.txt", "w") as file:
            file.write("This is the content of doc1")

        documents = load_documents(folder_path)
        self.assertEqual(len(documents), 1, "Should return a list with one document")
        self.assertIn(
            "This is the content of doc1",
            documents,
            "First document content mismatch",
        )


if __name__ == "__main__":
    unittest.main()
