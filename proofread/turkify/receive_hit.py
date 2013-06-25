from boto.mturk.connection import MTurkConnection
 
ACCESS_ID ='AKIAITMHLQDVTLTSK6PA'
SECRET_KEY = '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'
HOST = 'mechanicalturk.sandbox.amazonaws.com'
 
# this method is here because "get_reviewable_hits" only returns up to 100
def get_all_reviewable_hits(mtc):
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
 
mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)

#hits is a list of BOTO HITs objects
hits = get_all_reviewable_hits(mtc)
 
#hits -- hit = many assignments, one per worker00 assigment = answer --

#A 'question form answer' is the single answer to a single question of your form
#An 'answer' element is the set of all the 'question form answer' of your QuestionForm
#An 'assignment' is the set of all the 'answers' of the same worker for a given hit
#   In practice each worker can give just 1 'answer' to the hit, for that the assignment will contain always just one 'answer'.
#A 'hit' is a set of identical assignments given to different workers
#hits is a list of hits objects

for hit in hits:
    assignments = mtc.get_assignments(hit.HITId)
    for assignment in assignments:
        print "Answers of the worker %s" % assignment.WorkerId
        for question_form_answer in assignment.answers[0]: #assignment.answers is a list of answers that always contains only one element
            print question_form_answer.fields[0]

            for value in question_form_answer.fields:
                print "%s" % (value)


            #for key, value in question_form_answer.fields:
            #    print "%s: %s" % (key,value)
        mtc.approve_assignment(assignment.AssignmentId)
        print "--------------------"
    mtc.disable_hit(hit.HITId)