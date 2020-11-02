from flask import Flask
from flask import request
from flask import Flask, render_template
from statemachine import StateMachine, State


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


app = Flask(__name__)

editor_state = EditorStateMachine()


@app.route('/')
def index():
    return render_template('index.html', editor_Idle=editor_state.is_idle, rating_dd='')


@app.route('/get_task', methods=['GET', 'POST'])
def get_task():
    
    task = request.form['task_dd']
    editor_state.assigning()
    print(task)
    return render_template('assign.html', rating_dd='')


@app.route('/assign_article', methods=['GET', 'POST'])
def assign_article():
    editor_state.assign_ready()
    return 'Article Assigned'


if __name__=="__main__":
    app.run()