from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink, signals


class HackerProfile(models.Model):
    AVAILABILITY_CHOICES = [
        (0, 'Unspecified'),
        (1, 'Not available'),
        (2, 'Available for work'),
        (3, 'Available for contracts'),
        (4, 'Contact for availability'),
    ]
    
    user = models.OneToOneField(User)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    # Personal info
    birthdate = models.DateField(blank=True)
    
    # Contact info
    preferred_contact_email = models.EmailField(blank=True, verbose_name='Contact email')
    availability = models.PositiveSmallIntegerField(choices=AVAILABILITY_CHOICES, default=0)
    website = models.URLField(blank=True)
    
    # Social networking info
    twitter_username = models.CharField(max_length=64, blank=True, verbose_name='Twitter')
    facebook_username = models.CharField(max_length=64, blank=True, verbose_name='Facebook')
    tumblr_username = models.CharField(max_length=64, blank=True, verbose_name='Tumblr')
    github_username = models.CharField(max_length=64, blank=True, verbose_name='GitHub')
    stackoverflow_userid = models.PositiveIntegerField(blank=True, null=True,
        verbose_name='Stack Overflow', help_text='Stack Overflow user ID number')
    
    @property
    def contact_email(self):
        return self.preferred_contact_email or self.user.email
    
    def __unicode__(self):
        return u"Profile: %s" % self.user.username
    
    @permalink
    def get_absolute_url(self):
        return ('people_profile', (), {'username': self.user.username})

    class Meta:
        verbose_name = 'profile'


def create_profile(sender, *args, **kwargs):
    user = kwargs['instance']
    profile, created = HackerProfile.objects.get_or_create(user=user)
signals.post_save.connect(create_profile, sender=User)
