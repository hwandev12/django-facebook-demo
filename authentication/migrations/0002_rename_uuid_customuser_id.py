# Generated by Django 4.1.4 on 2023-01-07 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='uuid',
            new_name='id',
        ),
    ]
