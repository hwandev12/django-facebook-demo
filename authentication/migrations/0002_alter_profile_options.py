# Generated by Django 4.1.4 on 2023-01-09 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('special_status', 'Can edit profiles')]},
        ),
    ]