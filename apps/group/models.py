from django.db import models

from apps.user.models import User


class Team(models.Model):
    name = models.CharField('Name', max_length=255)
    users = models.ManyToManyField(User, related_name='teams', verbose_name='Users')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

