from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('guest', 'date', 'time', 'people', 'rating',)
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
            'guest': forms.HiddenInput(),
        }