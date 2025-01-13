import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.retriever import retrieve_documents


class TestRetriever(unittest.TestCase):
    def test_retriever_documents(self):
        documents = [
            "This is the first document",
            "This is the second document",
            "This is the third document",
        ]
        query = "document"
        results = retrieve_documents(query, documents)

        self.assertEqual(len(results), 3, "Should return all 3 documents")
        self.assertIn(
            "This is the second document", results, "Relevant document missing"
        )

    def test_retrieve_douments_empty(self):
        query = "xyz"
        results = retrieve_documents(query, [])
        self.assertEqual(len(results), 0, "Should return empty list")


if __name__ == "__main__":
    unittest.main()
