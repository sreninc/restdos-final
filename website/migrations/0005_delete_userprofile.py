# Generated by Django 3.2.7 on 2021-10-25 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]