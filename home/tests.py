from django.test import TestCase
from .apps import HomeConfig
from django.apps import apps


# Create your tests here.

class HomeTest(TestCase):

    # Test view

    def test_home_view(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    # Test apps

    def test_checkout_apps(self):
        self.assertEqual(HomeConfig.name, 'home')
        self.assertEqual(apps.get_app_config('home').name, 'home')