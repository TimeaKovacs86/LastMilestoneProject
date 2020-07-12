from django.contrib.auth.models import User
from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django.apps import apps
from .apps import AccountConfig


# Create your tests here.
class AccountsTestCase(TestCase):
    def setUp(self):
        """ Create a mock user for testing """
        self.credentials = {
            'username': 'Test_User',
            'password': 'Test_User_Password'
        }
        User.objects.create_user(**self.credentials)

    # Testing the views

    def test_admin_site(self):
        """ Test Admin login """
        page = self.client.get("/admin/login/")
        self.assertEqual(page.status_code, 200)

    def test_arrive_at_login_page(self):
        """ Test login redirection view """
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_login(self):
        """ Test user's status and it is actively log in after login """
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

    def test_arrive_at_registration_page(self):
        """ Test arriving on the register page and use the correct template """
        page = self.client.get("/accounts/registration/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")

    def test_arrive_at_profile_page(self):
        """ Test arriving on the profile page and use the correct template """
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")

    # Ask the mentor about this
    def test_logout_page(self):
        """ Test the logout functionality """
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        page = self.client.get("/accounts/logout/")
        self.assertRedirects(page, '/', status_code=302)

    def test_password_reset(self):
        """ Test the password reset page view """
        page = self.client.get("/accounts/password-reset/")
        self.assertEqual(page.status_code, 200)

    def test_edit(self):
        """ Test for edit user profile view """
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/accounts/profile/edit/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit.html")

    def test_change_password(self):
        """ Test for change password view """
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/accounts/profile/change-password/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "change-password.html")

    # Testing the forms

    def test_right_login_form(self):
        """ Test the UserLoginForm """
        form_data = {'username': 'TimeaKovacs', 'password': 'Test_password'}
        form = UserLoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_username_login_form(self):
        """ Test the UserLoginForm """
        form_data = {'username': '', 'password': 'Test_password'}
        form = UserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_missing_password_login_form(self):
        """ Test the UserLoginForm """
        form_data = {'username': 'TimeaKovacs', 'password': ''}
        form = UserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_UserRegistrationForm(self):
        """ Test UserRegistrationForm validation """
        form_data = {
            "first_name": "first_name",
            "last_name": "",
            "email": "email",
            "username": "username",
            "password1": "password1",
            "password2": "password2"
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_account_apps(self):
        self.assertEqual(AccountConfig.name, 'accounts')
        self.assertEqual(apps.get_app_config('accounts').name, 'accounts')