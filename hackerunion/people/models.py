from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink, signals


class HackerProfile(models.Model):
    user = models.OneToOneField(User)
    preferred_contact_email = models.EmailField(blank=True, verbose_name='Contact email')
    twitter_username = models.CharField(max_length=64, blank=True)
    facebook_username = models.CharField(max_length=64, blank=True)
    tumblr_username = models.CharField(max_length=64, blank=True)
    
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
