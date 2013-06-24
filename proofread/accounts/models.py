from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils.translation import ugettext_lazy as _

# define a get_absolute_url() method on user that returns account home

class UserAccount(AbstractUser):
    balance = models.DecimalField(
        "account balance (USD)",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        default=0,
    )

    def get_absolute_url(self):
        return "/"
