from django import forms
from .models import Guest


class GuestDetailsForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'email', 'mobile', 'dob',  'sms_marketing', 'sms_transactional', 'rating', 'service_notes', 'kitchen_notes', 'allergen_notes',)


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'mobile': 'Mobile',
            'dob': 'Date of Birth', 
            # 'guest_since':  'Guest Since', 
            'sms_marketing': 'SMS Marketing Consent', 'sms_transactional': 'SMS Transactional Consent', 
            'rating': 'Guest Rating', 
            'service_notes': 'Service Notes', 
            'kitchen_notes': 'Kitchen Notes', 
            'allergen_notes': 'Allergen & Intollerances Notes',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False