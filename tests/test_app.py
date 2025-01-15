import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_app_creation(self):
        self.assertIsNotNone(self.app)

    def test_routes_registration(self):
        response = self.client.get("/api/chat")
        self.assertEqual(
            response.status_code, 405
        )  # 405 tells us that server knows the request method but target resource doesn't support it as in our case we are trying to access GET method on /api/chat which only supports POST method


if __name__ == "__main__":
    unittest.main()
