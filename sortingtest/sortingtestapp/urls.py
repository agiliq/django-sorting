from django.conf.urls import patterns

urlpatterns = patterns('sortingtestapp.views',
                      (r'^$', 'index'),
                      (r'^xxx/$', 'index2'), )
