# Generated by Django 5.0.2 on 2024-03-11 20:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0002_episode_created_at_episode_is_active_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='user',
        ),
        migrations.AddField(
            model_name='episode',
            name='user',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='user_episodes', to=settings.AUTH_USER_MODEL),
        ),
    ]
