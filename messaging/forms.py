from django import forms

from .models import MessagingCampaign

class MessagingCampaignForm(forms.ModelForm):
    class Meta:
        model = MessagingCampaign
        fields = '__all__'