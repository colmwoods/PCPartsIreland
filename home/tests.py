from django.test import TestCase, Client, override_settings
from django.urls import reverse

# Create your tests here.
@override_settings(SECURE_SSL_REDIRECT=False)
class HomeViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("home")

    def test_home_page_loads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")