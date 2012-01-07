from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models


def alphanumeric_subdomains(subdomain):
    for ch in subdomain:
        if not ch.isalnum():
            raise ValidationError('Subdomains must be alphanumeric.')


class ChapterManager(models.Manager):
    def get_default_chapter(self, request=None):
        if request and request.user.is_authenticated():
            return request.user.get_profile().chapter
        return self.all()[0]


class Chapter(models.Model):
    subdomain = models.CharField(max_length=16, unique=True,
        validators=[alphanumeric_subdomains])
    name = models.CharField(max_length=64, unique=True, verbose_name='location')
    
    objects = ChapterManager()
    
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
