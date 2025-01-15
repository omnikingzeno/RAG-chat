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


if __name__ == "__main__":
    unittest.main()
