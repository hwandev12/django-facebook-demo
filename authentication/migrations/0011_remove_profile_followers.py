# Generated by Django 4.1.4 on 2023-01-17 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_profile_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
    ]
