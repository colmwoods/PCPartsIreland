from django.test import TestCase, Client, override_settings
from django.urls import reverse
from unittest.mock import patch
from decimal import Decimal

from products.models import Product
from checkout.models import Order, OrderLineItem

# Create your tests here.
@override_settings(
    SECURE_SSL_REDIRECT=False,
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
)
class CheckoutTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.product = Product.objects.create(
            name="Test Product",
            price=Decimal("100.00"),
            stock=10
        )

        session = self.client.session
        session["bag"] = {str(self.product.id): 2}
        session["currency"] = "EUR"
        session.save()

        self.checkout_url = reverse("checkout")

        self.valid_form_data = {
            "full_name": "John Doe",
            "email": "john@example.com",
            "phone_number": "123456789",
            "postcode": "A1B2C3",
            "town_or_city": "Dublin",
            "street_address1": "123 Test Street",
            "street_address2": "",
            "county": "Dublin",
            "client_secret": "testsecret_secret_123",
        }

    @patch("stripe.PaymentIntent.create")
    def test_checkout_get_renders_page(self, mock_stripe):
        mock_stripe.return_value.client_secret = "test_secret"

        response = self.client.get(self.checkout_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout.html")

    @patch("stripe.PaymentIntent.create")
    def test_checkout_post_creates_order(self, mock_stripe):
        mock_stripe.return_value.client_secret = "test_secret"

        response = self.client.post(self.checkout_url, self.valid_form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderLineItem.objects.count(), 1)

        order = Order.objects.first()
        self.assertEqual(order.lineitems.first().quantity, 2)

    @patch("checkout.views.send_mail")
    def test_checkout_success_deducts_stock_and_clears_bag(self, mock_mail):
        order = Order.objects.create(
            full_name="John Doe",
            email="john@example.com",
            phone_number="123456789",
            postcode="A1B2C3",
            town_or_city="Dublin",
            street_address1="123 Test Street",
            street_address2="",
            county="Dublin",
            order_total=Decimal("200.00"),
            delivery_cost=Decimal("0.00"),
            grand_total=Decimal("200.00"),
        )

        OrderLineItem.objects.create(
            order=order,
            product=self.product,
            quantity=2,
        )

        session = self.client.session
        session["bag"] = {str(self.product.id): 2}
        session.save()

        response = self.client.get(
            reverse("checkout_success", args=[order.order_number])
        )

        self.product.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.product.stock, 8)
        self.assertNotIn("bag", self.client.session)
