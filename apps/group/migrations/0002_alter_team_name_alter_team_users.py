# Generated by Django 4.2 on 2024-01-11 21:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='users',
            field=models.ManyToManyField(related_name='teams', to=settings.AUTH_USER_MODEL, verbose_name='Users'),
        ),
    ]
