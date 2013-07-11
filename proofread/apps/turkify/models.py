from datetime import datetime

from django.db import models
# from django.contrib.auth import get_user_model

from apps.projects.models import Project

task_types = ('edit', 'review')

###################
# Abstract Models #
###################

class HIT(models.Model):
    project = models.ForeignKey(Project)
    hit_id = models.CharField(max_length=126, blank=True, null=True, db_index=True)
    time_submitted = models.DateTimeField(auto_now_add=True, blank=True, null=True,
        help_text="time we submitted to turk")
    number_of_assignments = models.IntegerField()

    class Meta:
        abstract = True


class Assignment(models.Model):
    assignment_id = models.CharField(max_length=126, blank=True, null=True, db_index=True)
    time_received = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        help_text="time we received a viable correction from turk")
    # objects = AssignmentManager()

    class Meta:
        abstract = True


###############
# Edit Models #
###############

class EditHit(HIT):
    def receive(self):
        """
        Performed on receipt of all assignments
        """
        if self.number_of_assignments == 1:
            best_assignment = self.editassignment_set.all()[0]
        best_assignment.incorporate_changes()


class EditAssignment(Assignment):
    """
    to incorporate changes from a particular assignment instance, call
    assignment.incorporate_changes()
    """
    # assignment_id, time_received defined on Assignment
    edit_hit = models.ForeignKey(EditHit)
    edited = models.TextField(blank=True, null=True)
    chosen = models.BooleanField(default=False)

    def incorporate_changes(self):
        self.edit_hit.project.receive_from_turk( self.edited )


#################
# Review Models #
#################


class ReviewHit(HIT):
    def receive(self):
        """
        Performed on receipt of all assignments
        """


class ReviewAssignment(Assignment):
    # assignment_id, time_received defined on Assignment
    review_hit = models.ForeignKey(ReviewHit)
