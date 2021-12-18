from django.db import models

# Create your models here.
class MessagingCampaign(models.Model):
    filter = models.CharField(max_length=50)
    message = models.TextField()
    recipients = models.PositiveIntegerField()
    sms_length = models.PositiveIntegerField()
    sms_quantity = models.PositiveIntegerField()
    sms_cost = models.DecimalField(decimal_places=2, max_digits=7)
    low_cost = models.BooleanField()
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.filter