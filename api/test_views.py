import json
import unittest

from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()


    def test_base(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 404)


    def test_api_get(self):
        response = self.client.get('/api/num_to_english', {'number': '12345'}, 'application/json')
        self.assertEquals(response.status_code, 200)
        response_str = response.content.decode("utf-8")
        response_body = json.loads(response_str)
        self.assertEquals(response_body['num_in_english'], "twelve thousand, three hundred forty-five")


    def test_api_get_noninteger(self):
        response = self.client.get('/api/num_to_english', {'number': 'asdf'}, 'application/json')
        self.assertEquals(response.status_code, 400)


    def test_api_get_float(self):
        response = self.client.get('/api/num_to_english', {'number': 123.45}, 'application/json')
        self.assertEquals(response.status_code, 400)


    def test_api_post(self):
        response = self.client.post('/api/num_to_english', {'number': 12345}, 'application/json')
        self.assertEquals(response.status_code, 200)
        response_str = response.content.decode("utf-8")
        response_body = json.loads(response_str)
        self.assertEquals(response_body['num_in_english'], "twelve thousand, three hundred forty-five")


# c.get(path + '?number=12345')  # expected: returns parsed json string with status code 200
# c.get(path + '?number=123.45')  # expected: fails with status code 400
# c.get(path + '?number=asdf')  # expected: fails with status 400
# c.post(path, {'number': 12345}, HTTP_ACCEPT='application/json')  # expected:  parsed json with status code 200
# c.post(path, {'number': 123.45}, HTTP_ACCEPT='application/json')  # expected: fails with status 400
# c.post(path, {'number': "asdf"}, HTTP_ACCEPT='application/json')  # expected: fails with status 400
