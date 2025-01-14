import unittest
import json
from app import app


class TestChatAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_chat_with_valid_message(self):
        response = self.client.post(
            "/chat",
            data=json.dumps({"message": "example query"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("response", data)
        self.assertTrue(len(data["response"]) > 0)

    def test_chat_with_empty_message(self):
        response = self.client.post(
            "/chat", data=json.dumps({"message": ""}), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

    if __name__ == "__main__":
        unittest.main()
