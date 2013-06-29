from django.views.generic import UpdateView

from apps.projects.models import Project
from apps.projects.forms import ProjectForm


class EditProject(UserProjectMixin, CreateView):
    template_name = "projects/edit.html"
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse("project_success")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewProject, self).form_valid(form)