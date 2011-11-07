from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template, redirect_to

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'base.html'}, name='homepage'),
    (r'^robots\.txt', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    
    (r'^chapters/', include('chapters.urls', namespace='chapters', app_name='chapters')),
    (r'^events/', include('events.urls', namespace='events', app_name='events')),
    (r'^people/', include('people.urls', namespace='people', app_name='people')),
    (r'^projects/', include('projects.urls', namespace='projects', app_name='projects')),
    
    url(r'^admin/', include(admin.site.urls)),
    
    # /users/ is the hardcoded Django root for auth users; redirect to people
    (r'^users/$', redirect_to, {'url': '/people/'}),
    (r'^users/(?P<username>[A-Za-z0-9]+)/$', redirect_to, {'url': '/people/%(username)s/'}),
)
