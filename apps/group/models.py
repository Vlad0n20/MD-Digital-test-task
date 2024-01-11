from django.db import models

from apps.user.models import User


class Team(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

