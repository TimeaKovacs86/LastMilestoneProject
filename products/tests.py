from django.test import TestCase
from .models import Product
from .apps import ProductsConfig
from django.apps import apps


# Create your tests here.
class ProductTest(TestCase):

    # Test view
    def test_product_view(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    # Test models

    def test_name(self):
        """ Test product name field """
        test_product = Product(name="A product")
        self.assertEqual(str(test_product.name), "A product")
        self.assertEqual(str(test_product.name), test_product.name)

    def test_description(self):
        """ Test product description field """
        test_product_1 = Product(description_section="Description")
        self.assertEqual(str(test_product_1.description_section), "Description")

    def test_str(self):
        """ Test product price field """
        test_product = Product(price=456)
        self.assertEqual(int(test_product.price), 456)

    def test_product_slug(self):
        """ Test product slug field """
        test_product_slug = Product(slug="slug_test")
        self.assertEqual(str(test_product_slug.slug), "slug_test")

    def test_checkout_apps(self):
        self.assertEqual(ProductsConfig.name, 'products')
        self.assertEqual(apps.get_app_config('products').name, 'products')
