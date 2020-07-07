from django.test import TestCase
from .forms import PurchaseForm, ClientForm


# Tests for the 'purchase' app


class TestPurchase(TestCase):

    def test_can_purchase_without_a_full_name(self):
        form = PurchaseForm({'phone_number': '00000000',
                             'country': 'England',
                             'region': 'London'})
        self.assertFalse(form.is_valid(), form.errors)

    def test_can_purchase_without_a_country(self):
        form = PurchaseForm({'full_name': 'A full name',
                             'phone_number': '00000000',
                             'region': 'London'})
        self.assertFalse(form.is_valid(), form.errors)

    def test_can_purchase_without_a_region(self):
        form = PurchaseForm({'full_name': 'A full name',
                             'phone_number': '00000000',
                             'country': 'England'})
        self.assertFalse(form.is_valid(), form.errors)

    def test_full_purchase_form_is_valid(self):
        form = PurchaseForm({'full_name': 'A full name',
                             'phone_number': '00000000',
                             'country': 'England',
                             'region': 'London'})
        self.assertTrue(form.is_valid(), form.errors)


class TestClient(TestCase):

    def test_can_create_client_with_blank_description(self):
        form = ClientForm({'client_url': 'https://www.wikipedia.org/',
                           'client_description': ''})
        self.assertFalse(form.is_valid(), form.errors)

    def test_can_create_client_with_no_url(self):
        form = ClientForm({'client_description': 'Description'})
        self.assertFalse(form.is_valid(), form.errors)

    def test_full_client_form_is_valid(self):
        form = ClientForm({'client_url': 'https://www.wikipedia.org/',
                           'client_description': 'Description',
                           'client_email': 'email@example.com'})
        self.assertTrue(form.is_valid(), form.errors)
