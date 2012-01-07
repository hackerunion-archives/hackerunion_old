from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from tagging.models import Tag


def title_not_new(title):
    if title.lower() == 'new':
        raise ValidationError('Your project may not be named New.')


class ActiveProjectManager(models.Manager):
    def get_query_set(self):
        default_qs = super(ActiveProjectManager, self).get_query_set()
        return default_qs.filter(is_active=True)


class Project(models.Model):
    creator = models.ForeignKey(User, related_name='projects')
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64, unique=True,
        validators=[title_not_new])
    slug = models.SlugField(max_length=64)
    descriptions = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='projects')
    is_active = models.BooleanField('Active?', default=True)
    
    objects = models.Manager()
    active_projects = ActiveProjectManager()
    
    def clean(self):
        projects = self.creator.projects.filter(is_active=True)
        if self.pk:
            projects = projects.exclude(pk=self.pk)
        if self.is_active and projects.exists():
            raise ValidationError('A user may only have 1 active project.')
    
    @models.permalink
    def get_absolute_url(self):
        return ('project', (), {'slug': self.slug})
    
    def __unicode__(self):
        return self.title
