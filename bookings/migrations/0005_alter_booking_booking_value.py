# Generated by Django 3.2.7 on 2021-10-31 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_booking_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_value',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
