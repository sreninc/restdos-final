from django.db import models

# Create your models here.
class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.first_name + ' ' + self.last_name