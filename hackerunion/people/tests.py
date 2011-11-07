from django.test import TestCase


class URLTestCase(TestCase):
    fixtures = ['people.yaml']
    
    def test_index(self):
        resp = self.client.get('/people/')
        self.assertEqual(resp.status_code, 200)
    
    def test_profile(self):
        resp = self.client.get('/people/jdraper/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/people/doesnotexist/')
        self.assertEqual(resp.status_code, 404)
