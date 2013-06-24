from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import (
        AuthenticationForm, UserCreationForm, UserChangeForm
    )

from settings.main_settings import STRIPE_SECRET_KEY

import stripe

def logout_view(request):
    next = request.REQUEST.get('next', '/')
    logout(request)
    return HttpResponseRedirect(next)


class PayStripe(TemplateView):
    template_name = "main.html"

    def post(self, request, *args, **kwargs):
        # Stripe server side code
        # Set your secret key: remember to change this to your live secret key in production
        # See your keys here https://manage.stripe.com/account
        stripe.api_key = STRIPE_SECRET_KEY

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
          charge = stripe.Charge.create(
              amount=5400, # amount in cents, again
              currency="usd",
              card=token,
              description="payinguser@example.com"
          )
        except stripe.CardError, e:
            # The card has been declined
            pass

        return HttpResponse(charge, content_type="application/json")
        return HttpResponseRedirect('/')