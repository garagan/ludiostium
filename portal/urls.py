from django.conf.urls import patterns, url
from portal.views import HomePageView

urlpatterns = patterns('',
    # Index
    url('^$', HomePageView.as_view(), name='home'
        ),
)
