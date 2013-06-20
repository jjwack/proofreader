from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

class Project(models.Model):
    user = models.ForeignKey( get_user_model() )
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    unedited = models.TextField(blank=True, null=True)
    edited = models.TextField(blank=True, null=True)

    time_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField('are we waiting for Turk response', default=False) 
    submitted = models.BooleanField(default=False)
    time_submitted = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    turk_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = "%d-%s" % (self.pk, slugify(self.title) )
        super(Project, self).save(*args, **kwargs)

    def submit_to_turk(self):
        self.active = True
        self.submitted = True
        self.time_submitted = datetime.now()
        self.save()
