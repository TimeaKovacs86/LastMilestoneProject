from .models import Order
from django import forms
from django.core.validators import RegexValidator


class MakePaymentForm(forms.Form):
    credit_card_number = forms.IntegerField(label='Credit card number', required=False, max_value=9999999999999999)
    cvv = forms.IntegerField(label='Security code (CVV)', required=False, max_value=999)
    expiry_month = forms.IntegerField(label='Month (MM)', required=False, min_value=1, max_value=12)
    expiry_year = forms.IntegerField(label='Year (YYYY)', required=False, min_value=2020, max_value=2035)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super(MakePaymentForm, self).clean()
        credit_card_number = cleaned_data.get('credit_card_number')
        cvv = cleaned_data.get('cvv')
        if not credit_card_number and cvv:
            raise forms.ValidationError("Error")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'phone_number',
            'country',
            'postcode',
            'town_or_city',
            'street_address',
        )
