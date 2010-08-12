from django.conf.urls.defaults import *




urlpatterns = patterns('sortingtestapp.views',
    (r'^$', 'index'),
    (r'^xxx/$', 'index2'),
    
)
