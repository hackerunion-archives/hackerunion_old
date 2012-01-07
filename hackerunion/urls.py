from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template, redirect_to
from people.views import signup

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'homepage.html'}, name='homepage'),
    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    
    url(r'^signup/$', signup, name='signup'),
    
    (r'^chapters/', include('chapters.urls')),
    (r'^events/', include('events.urls')),
    (r'^people/', include('people.urls')),
    (r'^projects/', include('projects.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    
    # /users/ is the hardcoded Django root for auth users; redirect to people
    (r'^users/$', redirect_to, {'url': '/people/'}),
    (r'^users/(?P<username>[A-Za-z0-9]+)/$', redirect_to, {'url': '/people/%(username)s/'}),
)
