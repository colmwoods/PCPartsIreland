from django.test import TestCase, Client, override_settings
from django.urls import reverse
from decimal import Decimal
from products.models import Product, Category

# Create your tests here.
@override_settings(SECURE_SSL_REDIRECT=False)
class ProductViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.category1 = Category.objects.create(name="ddr4")
        self.category2 = Category.objects.create(name="ddr5")

        self.product1 = Product.objects.create(
            name="DDR4 RAM",
            price=Decimal("100.00"),
            category=self.category1,
            description="Fast RAM",
            sku="RAM001",
            stock=10
        )

        self.product2 = Product.objects.create(
            name="DDR5 RAM",
            price=Decimal("150.00"),
            category=self.category2,
            description="Faster RAM",
            sku="RAM002",
            stock=10
        )

        self.products_url = reverse("products")

    def test_all_products_page_loads(self):
        response = self.client.get(self.products_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_category_filtering(self):
        response = self.client.get(self.products_url, {"category": "ddr4"})

        products = response.context["products"]

        self.assertEqual(products.count(), 1)
        self.assertEqual(products.first(), self.product1)


    def test_sort_by_price_desc(self):
        response = self.client.get(
            self.products_url,
            {"sort": "price", "direction": "desc"}
        )

        products = list(response.context["products"])
        self.assertEqual(products[0], self.product2)

    def test_product_detail_loads(self):
        response = self.client.get(
            reverse("product_detail", args=[self.product1.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

    def test_search_returns_results(self):
        response = self.client.get(
            reverse("product_search"),
            {"q": "DDR4"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.name)

    def test_search_no_results(self):
        response = self.client.get(
            reverse("product_search"),
            {"q": "NonExistentProduct"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/search_results.html")

    def test_search_suggestions_json(self):
        response = self.client.get(
            reverse("search_suggestions"),
            {"q": "DDR"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertIn(self.product1.name, response.content.decode())