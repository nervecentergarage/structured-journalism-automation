import requests
from flask import Flask, render_template
import ast
import datetime

app = Flask(__name__)

ctx = {'_id': '',
       'work_started': False,
       'next_action': None,
       'current_job': '',
       'max_total_jobs': 10,
        'parallel_jobs': 0,
       'max_consecutive_jobs': 1,
       'total_jobs': 0}

providerId = ''
Journalist_profile = {'first_name': 'Journalist A',
           'status': 'idle'}

Editor_profile = {'first_name': 'Editor',
                  'status': ''}

Publisher_profile = {'first_name': 'Publisher',
                     'status': ''}

def wait():
    print('Waiting for Assignment')
    Journalist_profile['status'] = 'Waiting'
    end_of_assignment = ctx['total_jobs'] >= ctx['max_total_jobs']
    assigned = not (ctx['current_job'] == '')
    ctx['parallel_jobs'] = 1
    if end_of_assignment:
        return workdaydone
    elif assigned:
        return work
    else:
        return wait

def work():
    print('Working on Assignment')
    ctx['total_jobs'] += 1
    ctx['work_started'] = True
    Journalist_profile['status'] = 'Working'
    Editor_profile['status'] = ''
    update_profile()
    order_dict = ast.literal_eval(ctx['current_job'])
    order_dict['status'] = 'Complete'
    update_order(str(order_dict))
    ctx['current_job'] = ''
    parallel_jobs = ctx['parallel_jobs']
    max_consecutive_jobs = ctx['max_consecutive_jobs']
    if parallel_jobs < max_consecutive_jobs:
        return wait
    else:
        return nofurtherassignment


def nofurtherassignment():
    print('Already working on an Assignment')
    if Journalist_profile['status'] == 'Working':
        return check_if_reviewed
    elif Journalist_profile['status'] == 'Reviewed':
        return check_if_completed
    else:
        return work

def check_if_reviewed():
    if Editor_profile['status'] == 'Approved': # Need to integrate with Editor code
        Journalist_profile['status'] = 'Reviewed'
        return nofurtherassignment
    elif Editor_profile['status'] == 'Rejected':
        ctx['total_jobs'] -= 1
        return work

def check_if_completed():
    if Editor_profile['status'] == 'Approved':
        return workdone

def workdone():
    Journalist_profile['status'] = 'Completed'
    ctx['work_started'] = False
    ctx['next_action'] = None
    ctx['current_job'] = ''
    return wait

def workdaydone():
    print('retiring')
    get_balance()
    drone_send_payment('fedex', str(ctx['current_fexcoins']))
    profile['status'] = 'retired'
    update_profile()
    print("drone is retired")

    return None


def update_profile():
    print('updating drone profile')
    svc = '/update_profile'
    params = '?user_id=' + ctx['drone_id'] + '&profile=' + str(profile)
    url = smart_contract + svc + params
    _msg = requests.get(url).content

#---------------------------------------------------------------------------------
ctx['next_action'] = wait

status_msg = {wait: 'waiting',
              work: 'working',
              nofurtherassignment: 'getting maintenance',
              pay_for_maintenance: 'paying for maintenance',
              retire: 'retiring drone',
              register_drone: 'registering_drone',
              update_profile: 'updating profile',
              update_order: 'updating order',
              None: 'drone is out of service'
              }


if __name__ == '__main__':
    app.run(debug=True, port=5001)
