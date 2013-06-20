from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from api.views import MainPage, ESLReceipt, ESLReceiptAPI

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', MainPage.as_view(), name="main"),
    url(r'^dashboard/$', TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),
    url(r'^submit_message/$', ESLReceipt.as_view(content_type="text/html"), name='submit_message'),
    url(r'^api/$', ESLReceiptAPI.as_view(content_type="application/json"), name='api'),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
