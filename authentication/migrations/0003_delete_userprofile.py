# Generated by Django 4.1.4 on 2023-01-01 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
