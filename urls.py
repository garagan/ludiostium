from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # Game portal URLs
    url(r'', include('portal.urls')),
)