from django.conf.urls import patterns, include, url
from django.contrib import admin


apiurls = patterns(
    '',
    url(r'', include('track.urls')),
)


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(apiurls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
