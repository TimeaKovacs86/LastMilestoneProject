from django.test import TestCase
from .models import Feed
from django.contrib.auth.models import User
from .apps import FeedConfig
from django.apps import apps


# Create your tests here.

class FeedTest(TestCase):
    def setUp(self):
        """ Create a mock user for testing """
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    # Test views
    def test_feed_with_login(self):
        """ Test login view page """
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/feed/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "feed.html")

    def test_feed_without_login(self):
        """ Test feed view page """
        page = self.client.get("/feed/")
        self.assertEqual(page.status_code, 302)
        page = self.client.get("/accounts/login/?next=/feed/")
        self.assertEqual(page.status_code, 200)

    # Test models
    def test_feed_title(self):
        """ Test feed title """
        test_feed_title = Feed(title="Feed title")
        self.assertEqual(str(test_feed_title.title), test_feed_title.title)

    def test_feed_description(self):
        """ Test feed description """
        test_feed_description = Feed(description="Feed description")
        self.assertEqual(str(test_feed_description.description), "Feed description")

    def test_checkout_apps(self):
        self.assertEqual(FeedConfig.name, 'feed')
        self.assertEqual(apps.get_app_config('feed').name, 'feed')