from boto.mturk.connection import MTurkConnection
 
ACCESS_ID ='AKIAITMHLQDVTLTSK6PA'
SECRET_KEY = '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'
HOST = 'mechanicalturk.sandbox.amazonaws.com'
 
# this method is here because "get_reviewable_boto_hits" only returns up to 100
def get_all_reviewable_hits():
    mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                            aws_secret_access_key=SECRET_KEY,
                            host=HOST)
    page_size = 50
    boto_hits = mtc.get_reviewable_hits(page_size=page_size)
    print "Total results to fetch %s " % boto_hits.TotalNumResults
    print "Request boto_hits page %i" % 1
    total_pages = float(boto_hits.TotalNumResults)/page_size
    int_total= int(total_pages)
    if(total_pages-int_total>0):
        total_pages = int_total+1
    else:
        total_pages = int_total
    pn = 1
    while pn < total_pages:
        pn = pn + 1
        print "Request boto_hits page %i" % pn
        temp_boto_hits = mtc.get_reviewable_hits(page_size=page_size,page_number=pn)
        boto_hits.extend(temp_boto_hits)
    return boto_hits
 
#for each boto_hit that is reviewable, 
def process_reviewable_hits():
    #boto_hits is a list of BOTO HITs objects
    boto_hits = get_all_reviewable_hits()

    #boto_hits -> boto_hit = many boto_assignments, one per worker -> assigment = 1 answer -> 

    #A 'question form answer' is the single answer to a single question of your form
    #An 'answer' element is the set of all the 'question form answer' of your QuestionForm
    #An 'assignment' is the set of all the 'answers' of the same worker for a given boto_hit
    #   In practice each worker can give just 1 'answer' to the boto_hit, for that the assignment will contain always just one 'answer'.
    #A 'boto_hit' is a set of identical boto_assignments given to different workers
    #boto_hits is a list of boto_hits objects

    for boto_hit in boto_hits:
        boto_assignments = mtc.get_assignments(boto_hit.HITId) #this only gets the completed boto_assignments. can you only call get_boto_assignments on reviewable boto_hits? 
        for boto_assignment in boto_assignments:

            #gets the edited text and assignment id 
            edited = boto_assignment.answers[0][0].fields[0] 

            #create and instantiate new assignment object in our database (should do it here?)
            #note: creating instance of a database model is differnet from creating instance of a regular Python class)
            #note: normally use Assignements.objects.create but we have custom new method
            assignment = Assignment.objects.new(boto_hit.HITId, boto_assignment.AssignmentId, edited)

            #incorporate_changes calls assignment.hit.project.receive_from_turk(assignment.edited)
            assignment.incorporate_changes()

            #print "Answers of the worker %s" % boto_assignment.WorkerId
            #for question_form_answer in boto_assignment.answers[0]: #assignment.answers is a list of answers that always contains only one element
            #    print question_form_answer.fields[0]
            #    for value in question_form_answer.fields:
            #        print "%s" % (value)

            #mtc.approve_assignment(boto_assignment.AssignmentId)
            print "--------------------"
        mtc.disable_hit(boto_hit.HITId)
    