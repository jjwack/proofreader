from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from apps.projects.models import Project

task_types = ('edit', 'review')

"""
When receiving an assignment, call Hit.objects.receive(assignment)
This will create the appropriate assignment.
"""

class HIT(models.Model):
    project = models.ForeignKey(Project)
    hit_id = models.CharField(max_length=126, blank=True, null=True, db_index=True)
    time_submitted = models.DateTimeField(blank=True, null=True,
        help_text="time we submitted to turk")
    number_of_assignments = models.IntegerField()


class Assignment(models.Model):
    assignment_id = models.CharField(max_length=126, blank=True, null=True, db_index=True)
    time_received = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        help_text="time we received a viable correction from turk")
    # objects = AssignmentManager()

    class Meta:
        abstract = True

# for hit in hits:
#     for assignment in hit.assignments:
#         assign = save_to_db(assignment)
#         assign.approve_edits()


