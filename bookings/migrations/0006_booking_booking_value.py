# Generated by Django 3.2.7 on 2021-10-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_booking_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_value',
            field=models.IntegerField(default=0),
        ),
    ]