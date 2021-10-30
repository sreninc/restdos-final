from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Guest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField('First Name', max_length=50, null=False, blank=False)
    last_name = models.CharField('Last Name', max_length=50, null=False, blank=False)
    mobile = models.CharField('Mobile', max_length=15, null=False, blank=False)
    email = models.EmailField('Email', max_length=50, null=False, blank=False)
    dob = models.DateField('Date of Birth', null=True, blank=True)
    guest_since = models.DateField('Guest Since', auto_now_add=True, null=False, blank=False)
    sms_marketing = models.BooleanField('SMS Marketing Consent', default=False)
    sms_transactional = models.BooleanField('SMS Transactional Consent', default=True)
    rating = models.IntegerField('Guest Rating', default=5, null=False, blank=False)
    service_notes = models.TextField('Service Notes', null=True, blank=True)
    kitchen_notes = models.TextField('Kitchen Notes', null=True, blank=True)
    allergen_notes = models.TextField('Allergen & Intollerances Notes', null=True, blank=True)
    deleted = models.BooleanField(default=False)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name