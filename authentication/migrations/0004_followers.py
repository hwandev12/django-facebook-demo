# Generated by Django 4.1.4 on 2023-01-14 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_following', models.ManyToManyField(related_name='user_following', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Followers',
                'verbose_name_plural': 'Add Followers',
            },
        ),
    ]