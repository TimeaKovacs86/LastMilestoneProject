from django.test import TestCase
from .apps import SearchConfig
from django.apps import apps


# Create your tests here.

class SearchTest(TestCase):

    # Test apps
    def test_checkout_apps(self):
        self.assertEqual(SearchConfig.name, 'search')
        self.assertEqual(apps.get_app_config('search').name, 'search')