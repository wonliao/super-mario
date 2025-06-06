import unittest
import os
from app import app, PRIZES, SPIN_LOG_FILE

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        if os.path.exists(SPIN_LOG_FILE):
            os.remove(SPIN_LOG_FILE)
        with open(SPIN_LOG_FILE, 'a', encoding='utf-8'):
            pass

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

    def test_spin_log_file(self):
        with open(SPIN_LOG_FILE, 'r', encoding='utf-8') as f:
            before = len(f.readlines())
        self.client.get('/spin')
        with open(SPIN_LOG_FILE, 'r', encoding='utf-8') as f:
            after = len(f.readlines())
        self.assertEqual(after, before + 1)

if __name__ == '__main__':
    unittest.main()
