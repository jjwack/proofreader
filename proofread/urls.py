from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from core.views import MainPage

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', MainPage.as_view(), name="main"),
    url(r'^dashboard/$', TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),

    url(r'^projects/', include('esl_receipt.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
