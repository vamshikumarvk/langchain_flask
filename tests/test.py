import unittest
import sys
import os
sys.path.append(os.path.abspath("."))
from app import app

class ChatAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_chat_endpoint(self):
        response = self.app.post('/chat', json={'question': 'What is capital of the USA?'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('answer', response.get_json())

if __name__ == '__main__':
    unittest.main()