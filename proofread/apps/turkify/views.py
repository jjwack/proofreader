from django.views.generic import FormView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from apps.projects.models import Project
from apps.projects.forms import ProjectForm


class DebugMixin(object):
    """
    For use in testing out a new view
    """
    def get_context_data(self, **kwargs):
        "This is to print your context variables during testing ONLY"
        context = super(DebugMixin, self).get_context_data(**kwargs)
        print "#########################"
        print "CONTEXT SENT TO TEMPLATE:"
        # import pdb; pdb.set_trace()
        for k, v in context.items():
            print "  %s: %s" % (k, v)
        print "DON'T FORGET TO REMOVE THIS MIXIN AFTER TESTING THE VIEW"
        print "#########################"
        return context


class EditProject(UpdateView):
    template_name = "turkify/edit.html"
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project_permalink', args=[self.project.slug])

    def form_valid(self, form):
        self.project = self.get_object()
        self.project.receive_from_turk(form.data['unedited'])
        return HttpResponseRedirect(self.get_success_url())
