from django.views.generic import FormView, UpdateView, View
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect, HttpResponse
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


#################
# Utility Views #
#################

from django.views.generic.detail import SingleObjectMixin
from .create_hit import make_edit_hit
from .receive_hit import receive_assignments

class SendProject(SingleObjectMixin, View):
    model = Project

    def get(self, request, *args, **kwargs):
        project = self.get_object()
        make_edit_hit(project)
        return HttpResponse("Sent project %d (%s)" % (project.pk, project.title))

class ReceiveAll(View):
    def get(self, request, *args, **kwargs):
        total = receive_assignments()
        return HttpResponse("Received %d HITs" % total)