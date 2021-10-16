from django import forms
from .models import Guest

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class GuestDetailsForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'email', 'mobile', 'dob',  'sms_marketing', 'sms_transactional', 'rating', 'service_notes', 'kitchen_notes', 'allergen_notes',)


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Marilyn',
            'last_name': 'Monroe',
            'email': 'marilyn.monroe@email.com',
            'mobile': '0891234567',
            'dob': '01/01/1990', 
            'service_notes': 'Service Notes', 
            'kitchen_notes': 'Kitchen Notes', 
            'allergen_notes': 'Allergen & Intollerances Notes',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        # for field in self.fields:
        #     if self.fields[field].required:
        #         placeholder = f'{placeholders[field]} *'
        #     else:
        #         placeholder = placeholders[field]
        #     self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # self.fields[field].label = False


class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'email', 'mobile', 'dob', 'rating',  'sms_marketing', 'sms_transactional',)


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'add-guest'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'add_guest'
        self.helper.add_input(Submit('submit', 'Submit'))

        placeholders = {
            'first_name': 'Marilyn',
            'last_name': 'Monroe',
            'email': 'marilyn.monroe@email.com',
            'mobile': '0891234567',
            'dob': '01/01/1990', 
            'service_notes': 'Service Notes', 
            'kitchen_notes': 'Kitchen Notes', 
            'allergen_notes': 'Allergen & Intollerances Notes', 
            'rating': 'Rating',
            'sms_marketing': 'SMS Marketing',
            'sms_transactional': 'SMS Transactional',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder