from django.test import TestCase, Client, override_settings
from django.urls import reverse
from faq.models import FAQ

# Create your tests here.



@override_settings(SECURE_SSL_REDIRECT=False)
class FAQTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.active_faq = FAQ.objects.create(
            question="Active Question?",
            answer="Active Answer",
            is_active=True
        )

        self.inactive_faq = FAQ.objects.create(
            question="Inactive Question?",
            answer="Inactive Answer",
            is_active=False
        )

        self.url = reverse("faq")

    def test_faq_page_loads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "faq/faq.html")

    def test_only_active_faqs_are_displayed(self):
        response = self.client.get(self.url)

        self.assertContains(response, self.active_faq.question)
        self.assertNotContains(response, self.inactive_faq.question)