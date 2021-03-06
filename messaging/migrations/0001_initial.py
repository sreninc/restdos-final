# Generated by Django 3.2.7 on 2021-12-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessagingCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('recipients', models.PositiveIntegerField()),
                ('sms_length', models.PositiveIntegerField()),
                ('sms_quantity', models.PositiveIntegerField()),
                ('sms_cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('low_cost', models.BooleanField()),
                ('created', models.DateField(auto_now=True)),
            ],
        ),
    ]
