# Generated by Django 3.2.7 on 2021-10-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(verbose_name='Booking Date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='people',
            field=models.IntegerField(default=2, verbose_name='Guest Rating'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='rating',
            field=models.IntegerField(default=5, verbose_name='Guest Rating'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(verbose_name='Booking Time'),
        ),
    ]