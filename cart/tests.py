from django.contrib.auth.models import User
from django.test import TestCase
from django.apps import apps
from .apps import CartConfig


# Create your tests here.
class CartTesCase(TestCase):
    def setUp(self):
        """ Create a mock user for testing """
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    # Testing the views

    def test_cart_without_login(self):
        """ Test the cart view template page without login """
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")

    def test_cart_login(self):
        """ Test cart view template page with login """
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")

    def test_cart_apps(self):
        self.assertEqual(CartConfig.name, 'cart')
        self.assertEqual(apps.get_app_config('cart').name, 'cart')