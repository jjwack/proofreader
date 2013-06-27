from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from decimal import Decimal

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
        return reverse("user_home")

    def add_dollars(self, dollars):
        self.balance += Decimal(dollars)
        self.save()

