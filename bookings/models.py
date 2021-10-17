from django.db import models

# Create your models here.
class Booking(models.Model):
    guest_id = models.ForeignKey('guests.Guest', null=True, blank=False, on_delete=models.SET_NULL)
    date = models.DateField('Booking Date', null=False, blank=False)
    time = models.TimeField('Booking Time', null=False, blank=False)
    people = models.IntegerField('People', default=2, null=False, blank=False)
    rating = models.IntegerField('Guest Rating', default=5, null=False, blank=False)
