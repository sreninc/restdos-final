# Generated by Django 3.2.7 on 2021-10-30 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='signup_monthly',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='signup_plan',
        ),
    ]