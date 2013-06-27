from django.conf.urls import patterns, include, url
from django.contrib import auth
from django.views.generic.base import TemplateView

from registration.backends.default.views import ActivationView

from .registration_fixed import RegistrationView
from .views import PayStripe, AccountHome

# a lot of this is taken from django-registration. check out the source for specifics:
# https://bitbucket.org/ubernostrum/django-registration/src/8f242e35ef7c004e035e54b4bb093c32bf77c29f/registration/auth_urls.py?at=default

urlpatterns = patterns('',
    # Do something better with this view, it's just a placeholder
    url(r'^$', AccountHome.as_view(), name="user_home"),

    url(r'^pay_stripe/?$', PayStripe.as_view(), name="pay_stripe"),
    url(r'^declined/?$', TemplateView.as_view(template_name="accounts/declined.html"), name="stripe_declined"),
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name="login"),

    url(r'^login/$', auth.views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', 'accounts.views.logout_view', name="logout"),
    url(r'^sign_up/$', RegistrationView.as_view(), name='sign_up'),

    url(r'^activate/complete/$', TemplateView.as_view(template_name='registration/activation_complete.html'), name='registration_activation_complete'),
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    url(r'^activate/(?P<activation_key>\w+)/$', ActivationView.as_view(), name='registration_activate'),
    url(r'^sign_up/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
    url(r'^sign_up/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'), name='registration_disallowed'),
    url(r'^password/change/$', auth.views.password_change, name='auth_password_change'),
    url(r'^password/change/done/$', auth.views.password_change_done, name='auth_password_change_done'),
    url(r'^password/reset/$', auth.views.password_reset, name='auth_password_reset'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth.views.password_reset_confirm, name='auth_password_reset_confirm'),
    url(r'^password/reset/complete/$', auth.views.password_reset_complete, name='auth_password_reset_complete'),
    url(r'^password/reset/done/$', auth.views.password_reset_done, name='auth_password_reset_done'),

)
