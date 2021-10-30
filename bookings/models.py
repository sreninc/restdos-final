from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):

    class Status(models.TextChoices):
        COMPLETED = 'COM',_('Completed')
        CONFIRMED = 'CON',_('Confirmed')
        CANCELLED = 'CAN',_('Cancelled')
        DENIED = 'DEN',_('Denied')
        NOSHOW = 'NOS',_('No-Show')
        REQUESTED = 'REQ',_('Requested')
        SEATED = 'SEA',_('Seated')
        TABLEREADY = 'TAB',_('Table Ready')
        WAITLIST = 'WAI',_('Waitlist')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    guest = models.ForeignKey('guests.Guest', null=True, blank=False, on_delete=models.SET_NULL)
    date = models.DateField('Booking Date', null=False, blank=False)
    time = models.TimeField('Booking Time', null=False, blank=False)
    people = models.IntegerField('People', default=2, null=False, blank=False)
    rating = models.IntegerField('Guest Rating', default=5, null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    status = models.CharField(
        max_length=3,
        choices=Status.choices,
        default=Status.REQUESTED,
    )
    deleted = models.BooleanField(default=False)
    booking_value = models.IntegerField(default=0, null=False, blank=False)
