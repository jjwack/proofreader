from django.db import models

class Message(models.Model):
    user = models.ForeignKey(User)