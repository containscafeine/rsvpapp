import requests
import unittest


class RSVPAppTest(unittest.TestCase):
    def test_data_request(self):
        post_address = 'http://localhost:5000/new'
        user_data = {'name': 'test_name', 'email': 'test_email@test_domain.com'}
        r = requests.post(post_address, user_data)
        self.assertEqual(r.status_code, 200)
