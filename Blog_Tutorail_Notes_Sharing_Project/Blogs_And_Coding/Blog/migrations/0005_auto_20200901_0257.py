# Generated by Django 3.0.7 on 2020-08-31 21:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0004_auto_20200901_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='Likes',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
