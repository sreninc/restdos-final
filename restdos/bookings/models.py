from django.db import models

# Create your models here.
class Booking(models.Model):
    guest_id = models.ForeignKey('guests.Guest', null=True, blank=False, on_delete=models.SET_NULL)
    date = models.DateField()
    time = models.DateField()
    people = models.IntegerField()
    rating = models.IntegerField()
