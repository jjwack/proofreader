from django.views.generic import View, TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, logout, login, get_user_model
from django.contrib.auth.forms import (
        AuthenticationForm, UserCreationForm, UserChangeForm
    )
from settings.main_settings import STRIPE_SECRET_KEY

import stripe

# https://stripe.com/docs/checkout
# https://stripe.com/docs/checkout/guides/flask


def logout_view(request):
    next = request.REQUEST.get('next', '/')
    logout(request)
    return HttpResponseRedirect(next)


class PayStripe(View):

    def post(self, request, *args, **kwargs):
        stripe.api_key = STRIPE_SECRET_KEY
        amount = int(request.POST['amount'])
        token = request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
          charge = stripe.Charge.create(
              amount = amount,
              currency = "usd",
              card = token,
              description = "user %d" % request.user.id
          )
          request.user.add_dollars(amount/100)
        except stripe.CardError, e:
            # The card has been declined
            return HttpResponseRedirect( reverse('user_home')+"?accepted=False" )

        next = request.POST.get('next', reverse('user_home')+"?accepted=True")
        # return HttpResponse(charge, content_type="application/json")
        return HttpResponseRedirect(next)

class AccountHome(TemplateView):
    template_name = "accounts/home.html"