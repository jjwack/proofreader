from django.views.generic import TemplateView

class PayStripe(TemplateView):
    template_name = "main.html"

    def POST(self, request, *args, **kwargs):
        # add stripe stuff
        return render_to_response({})