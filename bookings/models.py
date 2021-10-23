from django.db import models
from django.utils.translation import gettext_lazy as _

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

    guest = models.ForeignKey('guests.Guest', null=True, blank=False, on_delete=models.SET_NULL)
    date = models.DateField('Booking Date', null=False, blank=False)
    time = models.TimeField('Booking Time', null=False, blank=False)
    people = models.IntegerField('People', default=2, null=False, blank=False)
    rating = models.IntegerField('Guest Rating', default=5, null=False, blank=False)
    status = models.CharField(
        max_length=3,
        choices=Status.choices,
        default=Status.REQUESTED,
    )
    deleted = models.BooleanField(default=False)
