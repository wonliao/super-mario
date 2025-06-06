import unittest
from app import app, PRIZES

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_spin(self):
        response = self.client.get('/spin')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('index', data)
        self.assertIn('prize', data)
        self.assertIn(data['prize'], PRIZES)

if __name__ == '__main__':
    unittest.main()
