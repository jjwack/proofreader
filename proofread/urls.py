from django.conf.urls import patterns, include, url
from django.contrib import admin

from api.views import MainPage, ESLReceipt

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', MainPage.as_view(), name="main"),
    url(r'^api/', ESLReceipt.as_view(), name='api'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
