from django.db import models

from .abstract_models import HIT, Assignment


class EditHit(HIT):
    def receive(self):
        """
        Performed on receipt of all assignments
        """
        if self.number_of_assignments == 1:
            best_assignment = self.edit_assignments.all()[0]
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
        self.hit.project.receive_from_turk( self.edited )
