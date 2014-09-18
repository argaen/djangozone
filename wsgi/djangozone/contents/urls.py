from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'contents.views',
    url(r'^posts/$', 'posts_list', name='posts_list'),
    url(r'^posts/(?P<slug>[\w-]+)$', 'posts_detail', name='posts_detail'),
    url(r'^posts/tag/(?P<tag>\w+)$', 'posts_tags', name='posts_tags'),

    url(r'^news/$', 'news_list', name='news_list'),
    url(r'^news/(?P<slug>[\w-]+)$', 'news_detail', name='news_detail'),
    url(r'^news/tag/(?P<tag>\w+)$', 'news_tags', name='news_tags'),

)
