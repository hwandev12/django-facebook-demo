# Generated by Django 4.1.4 on 2023-01-17 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('following', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stream_following', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stream', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]