from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models


class Chapter(models.Model):
    subdomain = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=64, unique=True, verbose_name='location')
    
    @property
    def location(self):
        return self.name
    
    def get_absolute_url(self):
        site = Site.objects.get_current()
        if settings.DEBUG:
            return '/?c=%s' % self.subdomain
        else:
            return 'http://%s.%s' % (self.subdomain, site.domain)
    
    def __str__(self):
        return self.subdomain
    
    def clean(self):
        for ch in self.subdomain:
            if not ch.isalnum():
                raise ValidationError('Subdomains must be alphanumeric')
