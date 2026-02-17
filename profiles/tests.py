from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from decimal import Decimal

from profiles.models import UserProfile
from checkout.models import Order

# Create your tests here.
@override_settings(SECURE_SSL_REDIRECT=False)
class ProfileViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        self.profile_url = reverse("profile")

    def test_profile_requires_login(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)

    def test_profile_page_loads_when_logged_in(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(self.profile_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_profile_update(self):
        self.client.login(username="testuser", password="testpass123")

        response = self.client.post(self.profile_url, {
            "default_phone_number": "123456789",
            "default_postcode": "A1B2C3",
            "default_town_or_city": "Dublin",
            "default_street_address1": "Street 1",
            "default_street_address2": "Street 2",
            "default_county": "Dublin",
        })

        self.assertEqual(response.status_code, 200)

        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.default_town_or_city, "Dublin")

    def test_orders_display_on_profile(self):
        self.client.login(username="testuser", password="testpass123")

        profile = UserProfile.objects.get_or_create(user=self.user)[0]

        Order.objects.create(
            order_number="123456",
            user_profile=profile,
            full_name="Test User",
            email="test@test.com",
            phone_number="123456",
            postcode="A1",
            town_or_city="City",
            street_address1="Street",
            county="County",
            order_total=Decimal("100.00"),
            delivery_cost=Decimal("10.00"),
            grand_total=Decimal("110.00"),
            original_bag="{}",
            stripe_pid="testpid"
        )

        response = self.client.get(self.profile_url)

        self.assertContains(response, "123456")

    def test_order_history_view(self):
        profile = UserProfile.objects.get_or_create(user=self.user)[0]

        order = Order.objects.create(
            order_number="999999",
            user_profile=profile,
            full_name="Test User",
            email="test@test.com",
            phone_number="123456",
            postcode="A1",
            town_or_city="City",
            street_address1="Street",
            county="County",
            order_total=Decimal("100.00"),
            delivery_cost=Decimal("10.00"),
            grand_total=Decimal("110.00"),
            original_bag="{}",
            stripe_pid="testpid"
        )

        response = self.client.get(
            reverse("order_history", args=[order.order_number])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")