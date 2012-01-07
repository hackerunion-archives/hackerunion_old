from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from tagging.models import Tag


class Project(models.Model):
    creator = models.ForeignKey(User, related_name='projects')
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64)
    descriptions = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='projects')
    is_active = models.BooleanField('Active?', default=True)
    
    def clean(self):
        if self.title.lower() == 'new':
            raise ValidationError('Your project may not be named New.')
        if (self.is_active and
            self.creator.projects.filter(is_active=True).exists()):
            raise ValidationError('A user may only have 1 active project.')
    
    @models.permalink
    def get_absolute_url(self):
        return ('project', (), {'slug': self.slug})
    
    def __unicode__(self):
        return self.title
