from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'contents.views.posts_list', name='posts_list'),
    url(r'^contents/', include('contents.urls')),
    url(r'^about/$', 'common.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls)),
)
