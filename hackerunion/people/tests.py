from django.core.urlresolvers import reverse
from django.test import TestCase
from people.models import HackerProfile


class URLTestCase(TestCase):
    fixtures = ['people.yaml']
    
    def setUp(self):
        self.root_url = reverse('people_index')
    
    def test_index(self):
        resp = self.client.get(self.root_url)
        self.assertEqual(resp.status_code, 200)
    
    def test_profile(self):
        resp = self.client.get(self.root_url + 'jdraper/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(self.root_url + 'doesnotexist/')
        self.assertEqual(resp.status_code, 404)


class HackerProfileTestCase(TestCase):
    fixtures = ['people.yaml']
    
    def setUp(self):
        self.profile = HackerProfile.objects.get(pk=1)
    
    def test_contact_email(self):
        self.assertEqual(self.profile.contact_email, 'jdraper@gmail.com')
