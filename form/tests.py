from django.test import TestCase, Client, override_settings
from django.urls import reverse
from form.models import ContactMessage, ReturnRequest


@override_settings(SECURE_SSL_REDIRECT=False)
class FormViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.contact_url = reverse("contact")
        self.success_url = reverse("success")
        self.return_url = reverse("return_request")
        self.return_success_url = reverse("return_success")

        self.valid_contact_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "phone": "123456789",
            "message": "Test contact message",
        }

        self.valid_return_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "order_number": "12345",
            "product_name": "Test Product",
            "reason": "faulty",
            "message": "Item arrived damaged",
        }

    def test_contact_page_loads(self):
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "form/contact.html")

    def test_contact_form_valid_submission(self):
        response = self.client.post(self.contact_url, self.valid_contact_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.success_url)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_form_invalid_submission(self):
        response = self.client.post(self.contact_url, {})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_success_page_loads(self):
        response = self.client.get(self.success_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "form/success.html")

    def test_return_request_valid_submission(self):
        response = self.client.post(self.return_url, self.valid_return_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.return_success_url)
        self.assertEqual(ReturnRequest.objects.count(), 1)

    def test_return_success_page_loads(self):
        response = self.client.get(self.return_success_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "form/return_success.html")
