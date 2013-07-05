from boto.mturk.connection import MTurkConnection

from .edit_models import EditHit, EditAssignment
from .review_models import ReviewHit, ReviewAssignment

ACCESS_ID ='AKIAITMHLQDVTLTSK6PA'
SECRET_KEY = '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'
HOST = 'mechanicalturk.sandbox.amazonaws.com'

# references
# http://www.toforge.com/2011/05/boto-mturk-tutorial-fetch-results-and-pay-workers/
# http://www.toforge.com/2011/04/boto-mturk-tutorial-create-hits/

def get_all_reviewable_hits(mtc):
    """
    Only returns hits that have all assignments returned
    """
    page_size = 50
    hits = mtc.get_reviewable_hits(page_size=page_size)
    print "Total results to fetch %s " % hits.TotalNumResults
    print "Request hits page %i" % 1
    total_pages = float(hits.TotalNumResults)/page_size
    int_total= int(total_pages)
    if(total_pages-int_total>0):
        total_pages = int_total+1
    else:
        total_pages = int_total
    pn = 1
    while pn < total_pages:
        pn = pn + 1
        print "Request hits page %i" % pn
        temp_hits = mtc.get_reviewable_hits(page_size=page_size,page_number=pn)
        hits.extend(temp_hits)
    return hits


def receive_edit_hit(mtc, edit_hit):
    # is mtc going to close? would it be better to 
    # start a new session each time this is called?
    mtc.get_assignments( edit_hit.hit_id )
    boto_assignments = mtc.get_assignments( edit_hit.hit_id )
    for boto_assignment in boto_assignments:
        EditAssignment.objects.create(
            edit_hit = edit_hit
            assignment_id = boto_assignment.AssignmentId
            edited = boto_assignment.answers[0][0].fields[0] 
        )
    edit_hit.receive()
    mtc.disable_hit( edit_hit.hit_id )
    

def receive_review_hit(mtc, edit_hit):
    # mtc.get_assignments(boto_hit.HITId)
    pass


def receive_assignments():
    mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                            aws_secret_access_key=SECRET_KEY,
                            host=HOST)
    for boto_hit in get_all_reviewable_hits(mtc):
        edit_hit = EditHit.objects.get( hit_id=boto_hit.HITId, None )
        review_hit = ReviewHit.objects.get( hit_id=boto_hit.HITId, None )
        if edit_hit:
            receive_edit_hit(mtc, edit_hit)
        elif review_hit:
            receive_review_hit(mtc, review_hit)
        # Hit not found!