from django import forms
from .models import Purchase, Client


# Forms for the 'checkout' app

class PaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2037)]

    credit_card_number = forms.CharField(label='Credit card number',
                                         required=False)
    cvv = forms.CharField(label='Security code (CW)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES,
                                     required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES,
                                    required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = {'full_name', 'phone_number', 'country', 'region'}


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = {'client_email', 'client_url', 'client_description'}
