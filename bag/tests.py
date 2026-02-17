from django.test import TestCase, Client, override_settings
from django.urls import reverse
from products.models import Product


@override_settings(SECURE_SSL_REDIRECT=False)
class BagViewsTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.product = Product.objects.create(
            name="Test Product",
            price=10.00,
            stock=5
        )

        self.redirect_url = reverse('view_bag')

    def test_view_bag_loads(self):
        response = self.client.get(self.redirect_url)
        self.assertEqual(response.status_code, 200)

    def test_add_product_to_bag(self):
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {
                'quantity': 2,
                'redirect_url': self.redirect_url
            }
        )

        self.assertEqual(response.status_code, 302)

        session = self.client.session
        self.assertIn(str(self.product.id), session.get('bag', {}))
        self.assertEqual(session['bag'][str(self.product.id)], 2)

    def test_add_fails_when_stock_zero(self):
        self.product.stock = 0
        self.product.save()

        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {
                'quantity': 1,
                'redirect_url': self.redirect_url
            }
        )

        self.assertEqual(response.status_code, 302)

        session = self.client.session
        self.assertNotIn(str(self.product.id), session.get('bag', {}))

    def test_adjust_quantity(self):
        session = self.client.session
        session['bag'] = {str(self.product.id): 2}
        session.save()

        response = self.client.post(
            reverse('adjust_bag', args=[self.product.id]),
            {'quantity': 3}
        )

        self.assertEqual(response.status_code, 302)

        session = self.client.session
        self.assertEqual(session['bag'][str(self.product.id)], 3)

    def test_adjust_removes_if_zero(self):
        session = self.client.session
        session['bag'] = {str(self.product.id): 2}
        session.save()

        response = self.client.post(
            reverse('adjust_bag', args=[self.product.id]),
            {'quantity': 0}
        )

        self.assertEqual(response.status_code, 302)

        session = self.client.session
        self.assertNotIn(str(self.product.id), session.get('bag', {}))

    def test_remove_from_bag(self):
        session = self.client.session
        session['bag'] = {str(self.product.id): 2}
        session.save()

        response = self.client.post(
            reverse('remove_from_bag', args=[self.product.id])
        )

        self.assertEqual(response.status_code, 200)

        session = self.client.session
        self.assertNotIn(str(self.product.id), session.get('bag', {}))
