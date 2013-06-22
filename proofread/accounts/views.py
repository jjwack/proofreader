from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
import stripe

class PayStripe(TemplateView):
    template_name = "main.html"

    def post(self, request, *args, **kwargs):
        print self.request.POST
        # Stripe server side code
        # Set your secret key: remember to change this to your live secret key in production
        # See your keys here https://manage.stripe.com/account
        stripe.api_key = "sk_test_mkGsLqEW6SLnZa487HYfJVLf"

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
          charge = stripe.Charge.create(
              amount=1000, # amount in cents, again
              currency="usd",
              card=token,
              description="payinguser@example.com"
          )
        except stripe.CardError, e:
          # The card has been declined
          pass



        # check the terminal output; self.request.POST is a dictionary
        # containing all the POST parameters.
        stripe_token = self.request.POST['stripeToken']
        return HttpResponseRedirect('/')