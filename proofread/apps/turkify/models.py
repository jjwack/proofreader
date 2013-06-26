from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from apps.projects.models import Project


class HIT(models.Model):
    project = models.ForeignKey(Project)
    hit_id = models.CharField(max_length=126, blank=True, null=True, db_index=True)
    time_submitted = models.DateTimeField(blank=True, null=True,
        help_text="time we submitted to turk")
    number_of_assignments = models.IntegerField()


class AssignmentManager(models.Manager):
    def new(self, hit_id, assignment_id, edited):
        """
        This will raise an exception if hit_id is not found
        """
        try:
            hit = HIT.objects.get(hit_id=hit_id)
        except:
            return "Hit object not found"
        assignment = self.model(
            hit=hit, assignment_id=assignment_id, edited=edited)
        assignment.save()
        return assignment


class Assignment(models.Model):
    """
    create new assignment with
    Assignment.objects.new(hit_id, assignment_id, edited)

    to incorporate changes from a particular assignment instance, call
    assignment.incorporate_changes()
    """
    hit = models.ForeignKey(HIT)
    assignment_id = models.CharField(max_length=126, blank=True, null=True, db_index=True)
    time_received = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        help_text="time we received a viable correction from turk")
    edited = models.TextField(blank=True, null=True)
    objects = AssignmentManager()

    def incorporate_changes(self):
        self.hit.project.receive_from_turk( self.edited )



# for hit in hits:
#     for assignment in hit.assignments:
#         assign = save_to_db(assignment)
#         assign.approve_edits()


