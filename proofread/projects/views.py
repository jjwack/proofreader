from django.views.generic import TemplateView, View, ListView, DetailView

from braces.views import JSONResponseMixin, AjaxResponseMixin

class ProjectsList(ListView):
    model = "add this"

class NewProject(TemplateView):
    template_name = "projects/new.html"

    def get(self, request, *args, **kwargs):
        context = {'response': 'You must POST a message'}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = {'response': 'Success!'}
        return self.render_to_response(context)


class NewProjectAPI(JSONResponseMixin, AjaxResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context = {'success': 0, 'message': 'You must POST a message'}
        return self.render_json_response(context)

    def post(self, request, *args, **kwargs):
        context = {'success': 1, 'message': "We got it!  You'll hear back soon"}
        return self.render_json_response(context)

class ProjectPermalink(DetailView):
    model = "add this"