from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', direct_to_template, {'template': 'base.html'}, name='homepage'),
    
    (r'^chapters/', include('chapters.urls')),
    (r'^people/', include('people.urls')),
    (r'^projects/', include('projects.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
