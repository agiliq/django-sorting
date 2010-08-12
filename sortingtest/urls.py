from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^sorttest/', include('sortingtestapp.urls')),
    url(r'^admin/(.*)', admin.site.root),
)
