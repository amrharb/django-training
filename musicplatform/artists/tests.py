from urllib import response
from django.test import TestCase
class ArtistTestCase(TestCase):
    def test_get_all_artists(self):
        response = self.client.get('/artists/')
        self.assertEqual(response.status_code,200)