# the default RegistrationView sends an activation email, the simple one doesn't
# also comment out the "register" method if using default
# from registration.backends.default.views import RegistrationView  as StupidRegistrationView
from registration.backends.simple.views import RegistrationView as StupidRegistrationView
from registration.forms import RegistrationForm as StupidRegistratonForm
from django.contrib.auth import authenticate, login, get_user_model # USE THIS!!!
from django.utils.translation import ugettext_lazy as _
from django import forms
from registration import signals

User = get_user_model()

class RegistrationForm(StupidRegistratonForm):
    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.

        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

class RegistrationView(StupidRegistrationView):
    form_class = RegistrationForm

    # comment this out to use email authentication
    def register(self, request, **cleaned_data):
        username, email, password = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
        User.objects.create_user(username, email, password)

        new_user = authenticate(username=username, password=password)
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user