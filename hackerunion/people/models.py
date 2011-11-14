from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals


class HackerProfile(models.Model):
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return u"Profile: %s" % self.user.username

    class Meta:
        verbose_name = 'profile'


def create_profile(sender, *args, **kwargs):
    user = kwargs['instance']
    profile, created = HackerProfile.objects.get_or_create(user=user)
signals.post_save.connect(create_profile, sender=User)
