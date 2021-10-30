from django import forms
from .models import Guest
from django.forms import HiddenInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class DateInput(forms.DateInput):
    input_type = 'date'


class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('user', 'first_name', 'last_name', 'email', 'mobile', 'dob', 'rating',  'sms_marketing', 'sms_transactional',)
        widgets = {
            'dob': DateInput(),
            'user': HiddenInput(),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'user': 'user',
            'first_name': 'Marilyn',
            'last_name': 'Monroe',
            'email': 'marilyn.monroe@email.com',
            'mobile': '0891234567',
            'dob': '', 
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


class NotesForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('service_notes', 'kitchen_notes', 'allergen_notes',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'service_notes': 'Service Notes', 
            'kitchen_notes': 'Kitchen Notes', 
            'allergen_notes': 'Allergen & Intollerances Notes',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder