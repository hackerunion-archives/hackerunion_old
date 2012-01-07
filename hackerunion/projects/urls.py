from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from projects.views import *

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'projects/base.html'}, name='projects_index'),
    url(r'^new/$', new_project, name='new_project'),
    url(r'^(?P<slug>[\w-]+)/$', project, name='project'),
)
