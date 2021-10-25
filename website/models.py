from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    mobile = models.CharField(max_length=20, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    signup_plan = models.CharField(max_length=50, null=False, blank=False)
    signup_monthly = models.IntegerField(default=100, null=False, blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


# Create your models here.
class Signup(models.Model):

    account_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    mobile = models.CharField(max_length=20, null=False, blank=False)
    # country = models.CharField(max_length=40, null=False, blank=False)
    # postcode = models.CharField(max_length=20, null=False, blank=False)
    # town_or_city = models.CharField(max_length=40, null=False, blank=False)
    # street_address_1 = models.CharField(max_length=80, null=False, blank=False)
    # street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    # county = models.CharField(max_length=80, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    signup_plan = models.CharField(max_length=50, null=False, blank=False)
    signup_monthly = models.IntegerField(default=100, null=False, blank=False)

    def _generate_account_number(self):
        """
        Generate a random, unique account number using UUID
        """
        return uuid.uuid4().hex


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the account number if it hasn't been set already.
        """
        
        if not self.account_number:
            self.account_number = self._generate_account_number()
        super().save(*args, **kwargs)