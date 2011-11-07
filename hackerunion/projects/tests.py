from django.test import TestCase


class URLTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/projects/')
        self.assertEqual(resp.status_code, 200)
