from django.conf.urls import patterns, include, url

from .views import PayStripe

urlpatterns = patterns('',
    # url(r'^$', MainPage.as_view(), name="main"),

    url(r'^pay_stripe/', PayStripe.as_view(), name="pay_stripe"),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^logout/$', 'accounts.views.logout_view', name="logout"),
)
