import os

from django.core.exceptions import ImproperlyConfigured

from boto.mturk.connection import MTurkConnection
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer

from .models import EditHit, EditAssignment, ReviewHit, ReviewAssignment

try:
    ACCESS_ID = os.environ.get('TURK_ACCESS_ID')
    SECRET_KEY = os.environ.get('TURK_SECRET_KEY')
    HOST = os.environ.get('TURK_HOST', 'mechanicalturk.sandbox.amazonaws.com')
except:
    raise ImproperlyConfigured("You must set the following environment\
variables: 'TURK_ACCESS_ID', 'TURK_SECRET_KEY', 'TURK_HOST'")


def get_mtc():
    return MTurkConnection(
        aws_access_key_id=ACCESS_ID,
        aws_secret_access_key=SECRET_KEY,
        host=HOST
    )