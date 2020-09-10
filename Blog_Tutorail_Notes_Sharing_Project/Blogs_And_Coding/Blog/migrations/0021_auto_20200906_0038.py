# Generated by Django 3.0.7 on 2020-09-05 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0020_discussionforum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussionforum',
            name='replyer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replyer', to=settings.AUTH_USER_MODEL),
        ),
    ]
