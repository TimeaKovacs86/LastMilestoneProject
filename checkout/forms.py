from .models import Order
from django import forms
from django.core.validators import RegexValidator


class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.IntegerField(label='Credit card number', required=False, max_value=9999999999999999)
    cvv = forms.IntegerField(label='Security code (CVV)', required=False, max_value=999)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
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
            'street_address1',
            'street_address2',
            'county',
        )
