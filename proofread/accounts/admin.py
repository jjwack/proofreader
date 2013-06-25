from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import UserAccount


# class UserAccountCreationForm(UserCreationForm):
#     class Meta:
#         model = UserAccount

#     def clean_username(self):
#         username = self.cleaned_data["username"]
#         try:
#             UserAccount.objects.get(username=username)
#         except UserAccount.DoesNotExist:
#             return username
#         raise forms.ValidationError(self.error_messages['duplicate_username'])

class UserAccountChangeForm(UserChangeForm):
    class Meta:
        model = UserAccount


class UserAccountAdmin(UserAdmin):
    # add_form = UserAccountCreationForm
    form = UserAccountChangeForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'balance', 'is_staff')
    # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'balance')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(UserAccount, UserAccountAdmin)
