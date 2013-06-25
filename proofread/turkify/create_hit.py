from boto.mturk.connection import MTurkConnection
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
 
ACCESS_ID ='AKIAITMHLQDVTLTSK6PA'
SECRET_KEY = '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'
HOST = 'mechanicalturk.sandbox.amazonaws.com'
 

def create_connection():
    mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                            aws_secret_access_key=SECRET_KEY,
                            host=HOST)
    return mtc

def get_account_balance(mtc):
    return mtc.get_account_balance()

#returns the hit ID
def new_edit_task(mtc, uneditted, assignments):
    
 
    title = 'Proofread a non-native English speaker\'s writing'
    description = 'Correct grammatical and word choice errors in the following email'
   
    keywords = 'proofreading, copyeditting, short'
     
    
    #---------------  BUILD OVERVIEW -------------------
     
    overview = Overview()
    overview.append_field('Title', 'Improve the email below')
    #overview.append(FormattedContent('<a target="_blank"'
    #                                    ' "href="http://www.toforge.com">'
    #                                    ' Mauro Rocco Personal Forge</a>'))
     
    #---------------  BUILD QUESTION 1 -------------------
     
    qc1 = QuestionContent()
    qc1.append_field('Title',uneditted)
     
    fta1 = FreeTextAnswer(default=uneditted, constraints=None, num_lines=25)

     
    q1 = Question(identifier='edits',
                                content=qc1,
                                answer_spec=AnswerSpecification(fta1),
                                is_required=True)
     
    #---------------  BUILD QUESTION 2 -------------------
     
    qc2 = QuestionContent()
    qc2.append_field('Title','any comments?')
     
    fta2 = FreeTextAnswer()
     
    q2 = Question(identifier="comments",
                                content=qc2,
                                answer_spec=AnswerSpecification(fta2))
     
    #--------------- BUILD THE QUESTION FORM -------------------
     
    question_form = QuestionForm()
    question_form.append(overview)
    question_form.append(q1)
    question_form.append(q2)
     
    #--------------- CREATE THE HIT -------------------
     
    hit_response = mtc.create_hit(questions=question_form,
                                 max_assignments=assignments,
                                 title=title,
                                 description=description,
                                 keywords=keywords,
                                 duration = 60*30,
                                 reward=0.05)

    print "created hit %s with %i assignments" % (hit_response[0].HITId, assignments)
    return hit_response[0].HITId

    