from django.test import TestCase
from .forms import UserRegistrationForm, UserLoginForm


# Tests for the 'accounts' app


class TestRegistration(TestCase):

    def test_can_register_with_just_a_username(self):
        form = UserRegistrationForm({'username': 'username'})
        self.assertFalse(form.is_valid(), form.errors)

    def test_can_register_with_just_an_email(self):
        form = UserRegistrationForm({'email': 'email@email.com'})
        self.assertFalse(form.is_valid(), form.errors)

    def test_can_register_with_only_one_password(self):
        form = UserRegistrationForm({'password1': 'password'})
        self.assertFalse(form.is_valid(), form.errors)

    def test_can_register_with_unmatched_passwords(self):
        form = UserRegistrationForm({'password1': 'first-password',
                                     'password2': 'second-password'})
        self.assertFalse(form.is_valid(), form.errors)

    def test_full_registration_form_is_valid(self):
        form = UserRegistrationForm({'username': 'testuser',
                                     'email': 'email@email.com',
                                     'password1': 'testformpassword1',
                                     'password2': 'testformpassword1'})
        self.assertTrue(form.is_valid(), form.errors)


class TestLogin(TestCase):

    def test_can_login_with_just_a_username(self):
        form = UserLoginForm({'username': 'username'})
        self.assertFalse(form.is_valid(), form.errors)

    def test_login_form_with_email_is_valid(self):
        form = UserLoginForm({'username': 'email@email.com',
                              'password': 'testformpassword1'})
        self.assertTrue(form.is_valid(), form.errors)

    def test_login_form_with_username_is_valid(self):
        form = UserLoginForm({'username': 'testuser',
                                     'password': 'testformpassword1'})
        self.assertTrue(form.is_valid(), form.errors)
