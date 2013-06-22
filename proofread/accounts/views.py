from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


class PayStripe(TemplateView):
    template_name = "main.html"

    def post(self, request, *args, **kwargs):
        print self.request.POST
        # add stripe stuff
        # check the terminal output; self.request.POST is a dictionary
        # containing all the POST parameters.
        stripe_token = self.request.POST['stripeToken']
        return HttpResponseRedirect('/')