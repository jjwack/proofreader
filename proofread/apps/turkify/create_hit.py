from .turk_core import *

def get_account_balance():
    mtc = get_mtc()
    return mtc.get_account_balance()


#returns the hit ID
def new_edit_task(unedited, assignments):
    """
    Create a new task to edit "unedited" where "assignments" is the number
    of assignments to create
    """
    mtc = get_mtc()

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
    qc1.append_field('Title',unedited)
    fta1 = FreeTextAnswer(default=unedited, constraints=None, num_lines=25)
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


def make_edit_hit(project, assignments=1):
    hit_id = new_edit_task(project.unedited, assignments)
    EditHit.objects.create(
        project = project,
        hit_id = hit_id,
        number_of_assignments = assignments
    )