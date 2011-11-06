from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from people.views import *

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'people/base.html'}, name='people'),
    url(r'^(?P<username>[A-Za-z0-9]+)/$', profile, name='profile'),
)
