from django.core.urlresolvers import reverse
from django.views.generic import (
    TemplateView,
    View,
    ListView,
    DetailView,
    CreateView,
    )

from braces.views import JSONResponseMixin, AjaxResponseMixin

from .models import Project
from .forms import ProjectForm


class ProjectsList(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        "This is to print your context variables during testing ONLY"
        context = super(ProjectsList, self).get_context_data(**kwargs)
        print "#########################"
        print "CONTEXT SENT TO TEMPLATE:"
        for k, v in context.items():
            print "  %s: %s\n" % (k, v)
        print "DON'T FORGET TO REMOVE THIS MIXIN AFTER TESTING THE VIEW"
        print "#########################"
        return context


class NewProject(CreateView):
    template_name = "projects/edit.html"
    model = Project
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


class ProjectPermalink(DetailView):
    model = Project