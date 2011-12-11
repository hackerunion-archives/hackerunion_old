from django.core.exceptions import ValidationError
from django.db import models


class Chapter(models.Model):
    subdomain = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=64, unique=True, verbose_name='location')
    
    @property
    def location(self):
        return self.name
    
    def __str__(self):
        return self.subdomain
    
    def clean(self):
        for ch in self.subdomain:
            if not ch.isalnum():
                raise ValidationError('Subdomains must be alphanumeric')
