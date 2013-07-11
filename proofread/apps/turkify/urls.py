from django.conf.urls import patterns, include, url

from .views import EditProject, SendProject, ReceiveAll

urlpatterns = patterns('',
    url(r'^send/(?P<pk>\d+)/$', SendProject.as_view(), name="send_project"),
    url(r'^receive/$', ReceiveAll.as_view(), name="receive_all"),
    url(r'^edit/(?P<pk>\d+)/$', EditProject.as_view(), name="edit_project"),
)
