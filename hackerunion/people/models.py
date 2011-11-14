from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink, signals


class ServiceType(models.Model):
    name = models.CharField(max_length=128)
    username_url = models.CharField(max_length=128,
        verbose_name='Username URL',
        help_text='Use %s as a placeholder for usernames')
    
    def __unicode__(self):
        return self.name


class Service(models.Model):
    user = models.ForeignKey(User, related_name='services')
    type = models.ForeignKey(ServiceType, related_name='users')
    username = models.CharField(max_length=128)
    
    def __unicode__(self):
        return u"%s: %s" % (self.type, self.username)


class HackerProfile(models.Model):
    user = models.OneToOneField(User)
    preferred_contact_email = models.EmailField(blank=True, verbose_name='Contact email')
    
    @property
    def contact_email(self):
        return self.preferred_contact_email or self.user.email
    
    def __unicode__(self):
        return u"Profile: %s" % self.user.username
    
    @permalink
    def get_absolute_url(self):
        return ('people:profile', (), {'username': self.user.username})

    class Meta:
        verbose_name = 'profile'


def create_profile(sender, *args, **kwargs):
    user = kwargs['instance']
    profile, created = HackerProfile.objects.get_or_create(user=user)
signals.post_save.connect(create_profile, sender=User)
