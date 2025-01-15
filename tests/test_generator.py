import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils.generator import generate_response


class TestGenerator(unittest.TestCase):
    def test_generate_response_with_documents(self):
        # Test with a list of valid documents
        query = "What is Python?"
        documents = [
            "Python is a programming language.",
            "It is widely used for web development, data analysis, and AI.",
        ]
        response = generate_response(query, documents)
        expected_response = (
            "For your query : 'What is Python?', here is what I found :\n\n"
            "Document 1 : \n Python is a programming language. \n\n"
            "Document 2 : \n It is widely used for web development, data analysis, and AI."
        )
        self.assertIn(response, expected_response)

    # def test_generate_response_with_empty_documents(self):
    #     # Test with an empty list of documents
    #     query = "What is Python?"
    #     documents = []
    #     response = generate_response(query, documents)
    #     expected_response = (
    #         "Relevant information based on your query:\n\n"
    #         "No relevant documents were found."
    #     )
    #     self.assertEqual(response, expected_response)

    # def test_generate_response_with_special_characters(self):
    #     # Test with documents containing special characters
    #     query = "Explain symbols"
    #     documents = [
    #         "Symbols include &, %, $, and @.",
    #         "They are often used in programming and mathematics.",
    #     ]
    #     response = generate_response(query, documents)
    #     expected_response = (
    #         "Relevant information based on your query:\n\n"
    #         "Symbols include &, %, $, and @.\n"
    #         "They are often used in programming and mathematics."
    #     )
    #     self.assertEqual(response, expected_response)

    # def test_generate_response_with_long_documents(self):
    #     # Test with excessively long documents
    #     query = "Tell me something long"
    #     documents = ["A" * 1000, "B" * 1000]  # 1000 'A's  # 1000 'B's
    #     response = generate_response(query, documents)
    #     expected_response = (
    #         "Relevant information based on your query:\n\n"
    #         + "A" * 1000
    #         + "\n"
    #         + "B" * 1000
    #     )
    #     self.assertEqual(response, expected_response)


if __name__ == "__main__":
    unittest.main()
