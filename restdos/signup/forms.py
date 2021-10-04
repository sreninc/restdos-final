from django import forms
from .models import Signup


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ('first_name', 'last_name', 'email', 'mobile', 'country', 'postcode', 'town_or_city', 'street_address_1', 'street_address_2', 'county', 'signup_plan', 'signup_monthly',)


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'mobile': 'Mobile',
            'country': 'Country',
            'postcode': 'Postcode',
            'town_or_city': 'Town/City',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'county': 'County',
            'signup_plan': 'Signup Plan',
            'signup_monthly': 'Signup Monthly',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False