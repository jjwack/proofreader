from django.conf.urls import patterns, include, url

from .views import EditProject

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', EditProject.as_view(), name="edit_project"),
)
