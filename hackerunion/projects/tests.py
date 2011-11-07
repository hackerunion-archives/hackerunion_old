from django.core.urlresolvers import reverse
from django.test import TestCase


class URLTestCase(TestCase):
    def setUp(self):
        self.root_url = reverse('projects:index')
    
    def test_index(self):
        resp = self.client.get(self.root_url)
        self.assertEqual(resp.status_code, 200)
