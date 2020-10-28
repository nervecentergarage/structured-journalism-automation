from statemachine import StateMachine, State
from flask import Flask, render_template, session, request
from flask_session import Session


class EditorStateMachine(StateMachine):
    idle = State('Idle', initial=True)
    assign = State('Assign')
    review = State('Review')
    send = State('Sending')

    assigning = idle.to(assign)
    reviewing = idle.to(review)
    sending = idle.to(send)
    assign_ready = assign.to(idle)
    review_ready = review.to(idle)
    sent_ready = send.to(idle)


class JounalistStateMachine(StateMachine):
    j_idle = State('Idle', initial=True)
    j_assign = State('Assignment')
    j_work = State('Work')
    j_wait = State('Wait')

    j_assigning = j_idle.to(j_assign)
    j_working = j_assign.to(j_work)
    j_waiting = j_work.to(j_wait)
    j_reworking = j_wait.to(j_work)
    j_finishing = j_wait.to(j_idle)


#
# class PublisherStateMachine(StateMachine):
#     j_idle = State('Idle', initial=True)
#     j_assign = State('Assignment')
#     j_work = State('Work')
#     j_wait = State('Wait')
#
#     j_assigning = j_idle.to(j_assign)
#     j_working = j_assign.to(j_work)
#     j_waiting = j_work.to(j_wait)
#     j_reworking = j_wait.to(j_work)
#     j_finishing = j_wait.to(j_idle)
#
#
# class ArticleStateMachine(StateMachine):
#     j_idle = State('Idle', initial=True)
#     j_assign = State('Assignment')
#     j_work = State('Work')
#     j_wait = State('Wait')
#
#     j_assigning = j_idle.to(j_assign)
#     j_working = j_assign.to(j_work)
#     j_waiting = j_work.to(j_wait)
#     j_reworking = j_wait.to(j_work)
#     j_finishing = j_wait.to(j_idle)


app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

journalist_state = JounalistStateMachine()
editor_state = EditorStateMachine()


@app.route('/')
def index():
    # session['e_previous_task'] = ''
    return render_template('index.html', editor_state='idle', task='')


# This method will show the task available to Editor
@app.route('/get_task', methods=['GET', 'POST'])
def get_task():
    task = request.form['task_dd']
    pre_task = request.form['previous_task']
    if editor_state.is_idle or pre_task == session['e_previous_task']:
        print(task)
        print(type(editor_state.current_state))
        e_state = ''
        # Need to add conditions of other tasks of Editor
        if task == 'assign':
            editor_state.assigning()
            e_state = 'assigning'
        elif task == 'review':
            editor_state.reviewing()
            e_state = 'reviewing'
        elif task == 'task_reviewed':
            article_name = request.form['article_dd']
            task = 'review_article'
            # write logic to redirect the editor to article page where he will accept or reject the article.
        elif task == 'task_assigned':
            editor_state.assign_ready()
            # journalist_state.j_assigning()
            e_state = 'ready'
            j_name = request.form['journalist_dd']
            a_name = request.form['article_dd']
            return a_name + ' has been assigned to ' + j_name
            # Add functionality to send notification to Journalist that he has a article to work on
        elif task == 'task_sent':
            editor_state.sending()
            e_state = 'sending'
        # elif task == 'task_assigned':
        #     editor_state.sent_ready()
        #     return 'Article sent to publisher'

        session['e_previous_task'] = task
        return render_template('index.html', task=task, editor_state=e_state)
    else:
        return 'Editor is busy.'


@app.route('/j_work_on_task', methods=['GET', 'POST'])
def work_on_task():
    journalist_state.j_working()
    # In this below page he will start working on the assigned article.
    return render_template('journalistWorking.html', rating_dd='')


@app.route('/j_submitted', methods=['GET', 'POST'])
def assigned_task():
    journalist_state.j_waiting()
    # Send notification to editor that task has been submitted for the review.
    # Here show the message that your task is submitted for the review.
    return render_template('JournalistWorking.html', rating_dd='')


if __name__ == "__main__":
    app.run()
