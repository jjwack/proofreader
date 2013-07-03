from django.db import models

from .abstract_models import HIT, Assignment

class ReviewHit(HIT):
    def receive(self):
        """
        Performed on receipt of all assignments
        """


class ReviewAssignment(Assignment):
    # assignment_id, time_received defined on Assignment
    review_hit = models.ForeignKey(ReviewHit)
