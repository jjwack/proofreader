from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import ESLReceipt, ESLReceiptAPI


urlpatterns = patterns('',
    url(r'^submit/$', ESLReceipt.as_view(content_type="text/html"), name='submit_message'),
    url(r'^submit.json$', ESLReceiptAPI.as_view(content_type="application/json"), name='api'),
)
