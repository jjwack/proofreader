from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import ProjectsList, NewProject, NewProjectAPI, ProjectPermalink


urlpatterns = patterns('',
    url(r'^$', ProjectsList.as_view(), name='projects'),
    url(r'^new/$', NewProject.as_view(), name='new_project'),
    url(r'^new/success/$', TemplateView.as_view(template_name='projects/success.html'), name='project_success'),
    # url(r'^new.json/$', NewProjectAPI.as_view(), name='api'),
    url(r'^(?P<slug>[\w-]+)/', ProjectPermalink.as_view(), name='project_permalink')
)
