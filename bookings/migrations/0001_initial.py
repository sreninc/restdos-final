# Generated by Django 3.2.7 on 2021-10-27 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guests', '0003_auto_20211016_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Booking Date')),
                ('time', models.TimeField(verbose_name='Booking Time')),
                ('people', models.IntegerField(default=2, verbose_name='People')),
                ('rating', models.IntegerField(default=5, verbose_name='Guest Rating')),
                ('status', models.CharField(choices=[('COM', 'Completed'), ('CON', 'Confirmed'), ('CAN', 'Cancelled'), ('DEN', 'Denied'), ('NOS', 'No-Show'), ('REQ', 'Requested'), ('SEA', 'Seated'), ('TAB', 'Table Ready'), ('WAI', 'Waitlist')], default='REQ', max_length=3)),
                ('deleted', models.BooleanField(default=False)),
                ('booking_value', models.IntegerField(default=0)),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='guests.guest')),
            ],
        ),
    ]
