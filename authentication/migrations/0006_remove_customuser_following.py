# Generated by Django 4.1.4 on 2023-01-17 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_customuser_following_delete_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='following',
        ),
    ]
