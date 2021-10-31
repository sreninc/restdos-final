# Generated by Django 3.2.7 on 2021-10-31 09:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='people',
            field=models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1)], verbose_name='People'),
        ),
    ]
