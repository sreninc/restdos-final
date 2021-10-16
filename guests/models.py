from django.db import models

# Create your models here.
class Guest(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    mobile = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    dob = models.DateField(null=True, blank=True)
    guest_since = models.DateField(auto_now_add=True, null=False, blank=False)
    sms_marketing = models.BooleanField(default=False)
    sms_transactional = models.BooleanField(default=True)
    rating = models.IntegerField(default=5, null=False, blank=False)
    service_notes = models.TextField(null=True, blank=True)
    kitchen_notes = models.TextField(null=True, blank=True)
    allergen_notes = models.TextField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name