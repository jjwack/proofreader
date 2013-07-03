from django.core.urlresolvers import reverse
from django.views.generic import (
    TemplateView,
    View,
    ListView,
    DetailView,
    CreateView,
    )

from braces.views import LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin

from .models import Project
from .forms import ProjectForm


class UserProjectMixin(LoginRequiredMixin):
    """
    Parent mixin for all project views.  It restricts access to logged-in users,
    and only returns projects specific to the user.  This should be the first
    thing you inherit from in defining a project view.
    """
    model = Project

    def get_queryset(self):
        if self.request.user.is_staff:
            return Project.objects.all().order_by('-time_created')
        return self.request.user.project_set.all().order_by('-time_created')


class ProjectsList(UserProjectMixin, ListView):
    pass


class NewProject(UserProjectMixin, CreateView):
    template_name = "projects/edit.html"
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("project_success")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewProject, self).form_valid(form)


class NewProjectAPI(JSONResponseMixin, AjaxResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context = {'success': 0, 'message': 'You must POST a message'}
        return self.render_json_response(context)

    def post(self, request, *args, **kwargs):
        context = {'success': 1, 'message': "We got it!  You'll hear back soon"}
        return self.render_json_response(context)


class ProjectPermalink(UserProjectMixin, DetailView):
    model = Project