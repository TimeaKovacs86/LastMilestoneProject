from django.contrib.auth.models import User
from django.test import TestCase
from django.apps import apps
from .models import Order
from .forms import MakePaymentForm, OrderForm
from .apps import CheckoutConfig


# Create your tests here.
class CheckoutTesCase(TestCase):
    def setUp(self):
        """ Create a mock user for testing """
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    # Testing the views

    def test_checkout_without_login(self):
        """ Test checkout page without login """
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 302)
        page = self.client.get("/accounts/login/?next=/checkout/")
        self.assertEqual(page.status_code, 200)

    def test_checkout_with_login(self):
        """ Test checkout page with login """
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")

    # Test models

    def test_checkout_full_name(self):
        """ Test full name field """
        test_model = Order(full_name="Timea Kovacs")
        self.assertEqual(str(test_model.full_name), "Timea Kovacs")

    def test_checkout_phone_number(self):
        """ Test phone number field """
        test_model = Order(phone_number=891234567)
        self.assertEqual(int(test_model.phone_number), 891234567)

    def test_checkout_country(self):
        """ Test country field """
        test_model = Order(country="Ireland")
        self.assertEqual(str(test_model.country), "Ireland")

    def test_checkout_postcode(self):
        """ Test postcode field """
        test_model = Order(postcode="Dublin 2")
        self.assertEqual(str(test_model.postcode), "Dublin 2")

    def test_checkout_town_or_city(self):
        """ Test town or city field """
        test_model = Order(town_or_city="Dublin")
        self.assertEqual(str(test_model.town_or_city), "Dublin")

    def test_checkout_street_address1(self):
        """ Test street address 1 field """
        test_model = Order(street_address1="Wintergarden Apartments 48, The Pine")
        self.assertEqual(str(test_model.street_address1), "Wintergarden Apartments 48, The Pine")

    def test_checkout_street_address2(self):
        """ Test street address 2 field """
        test_model = Order(street_address2="Pearse Street 107")
        self.assertEqual(str(test_model.street_address2), "Pearse Street 107")

    def test_checkout_county(self):
        """ Test county field """
        test_model = Order(county="Dublin")
        self.assertEqual(str(test_model.county), "Dublin")

    def test_checkout_email(self):
        """ Test email field """
        test_model = Order(email="test@test.com")
        self.assertEqual(str(test_model.email), "test@test.com")

    # Testing the forms
    def test_payment_login_form(self):
        """ Test the MakePaymentForm """
        form_data = {
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 3,
            'expiry_year': 2021,
            'stripe_id': 42}
        form = MakePaymentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_order_payment_login_form(self):
        """ Test the OrderForm """
        form_data = {
            'full_name': 'Timea Kovacs',
            'phone_number': 353891234567,
            'country': 'Ireland',
            'postcode': 'Dublin 2',
            'town_or_city': 'Dublin',
            'street_address1': 'Test Street',
            'street_address2': 'Test Street 2',
            'county': 'Dublin'
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Test apps.py

    def test_checkout_apps(self):
        self.assertEqual(CheckoutConfig.name, 'checkout')
        self.assertEqual(apps.get_app_config('checkout').name, 'checkout')
