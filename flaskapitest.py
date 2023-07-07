import unittest
from flask import Flask
from flask_testing import TestCase
from your_app import app

class APITestCase(TestCase):

    def create_app(self):
        return app

    def test_endpoint(self):
        # Test the endpoint of your Flask API
        response = self.client.post('/upload', data={'file': (open('path/to/test_file.pdf', 'rb'), 'test_file.pdf')})
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'expected_response', response.data)

if __name__ == '__main__':
    unittest.main()