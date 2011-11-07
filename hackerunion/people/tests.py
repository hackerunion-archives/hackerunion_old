from django.core.urlresolvers import reverse
from django.test import TestCase


class URLTestCase(TestCase):
    fixtures = ['people.yaml']
    
    def setUp(self):
        self.root_url = reverse('people:index')
    
    def test_index(self):
        resp = self.client.get(self.root_url)
        self.assertEqual(resp.status_code, 200)
    
    def test_profile(self):
        resp = self.client.get(self.root_url + 'jdraper/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(self.root_url + 'doesnotexist/')
        self.assertEqual(resp.status_code, 404)
