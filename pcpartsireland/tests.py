from django.test import TestCase, Client, override_settings
from django.urls import reverse


@override_settings(SECURE_SSL_REDIRECT=False)
class CurrencyViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_set_valid_currency(self):
        response = self.client.get(
            reverse("set_currency", args=["EUR"]),
            HTTP_REFERER="/"
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session.get("currency"), "EUR")

    def test_set_invalid_currency(self):
        response = self.client.get(
            reverse("set_currency", args=["INVALID"]),
            HTTP_REFERER="/"
        )

        self.assertEqual(response.status_code, 302)
        self.assertNotIn("currency", self.client.session)

    def test_redirects_to_referer(self):
        response = self.client.get(
            reverse("set_currency", args=["USD"]),
            HTTP_REFERER="/products/"
        )

        self.assertRedirects(response, "/products/")
