from django.contrib.auth.models import User
from django.db import models


class HackerProfile(models.Model):
    user = models.OneToOneField(User)

    class Meta:
        verbose_name = 'profile'
