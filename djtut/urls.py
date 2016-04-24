from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from polls import urls as polls_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'djtut.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include(polls_urls, namespace='polls')),
    # url(r'^(?P<path>.*)$', serve,
    #     {'document_root': '/home/sweidman/PycharmProjects/djtut/templates',
    #      'show_indexes': True}),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (url(r'^__debug__/', include(debug_toolbar.urls)),)
