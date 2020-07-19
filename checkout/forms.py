from .models import Order
from django import forms


class MakePaymentForm(forms.Form):
    credit_card_number = forms.IntegerField(label='Credit card number', required=False)
    cvv = forms.IntegerField(label='Security code (CVV)', required=False)
    expiry_month = forms.IntegerField(label='Month', required=False)
    expiry_year = forms.IntegerField(label='Year', required=False)
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
