from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'base.html'}, name='homepage'),
    
    (r'^chapters/', include('chapters.urls', namespace='chapters', app_name='chapters')),
    (r'^people/', include('people.urls', namespace='people', app_name='people')),
    (r'^projects/', include('projects.urls', namespace='projects', app_name='projects')),
    
    url(r'^admin/', include(admin.site.urls)),
)
