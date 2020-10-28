import requests
from flask import Flask, render_template
import ast
import datetime
Publisher_profile = {'first_name': 'Publisher',
                     'status': ''}
def wait():
    print('Waiting for the article from editor')
    Publisher_profile['status'] = 'Waiting'
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
    if Journalist_Profile['Status'] == 'Completed':
        Publisher_profile['Status'] = 'Working'
    ctx['current_job'] = ''
    parallel_jobs = ctx['parallel_jobs']
    max_consecutive_jobs = ctx['max_consecutive_jobs']
    if parallel_jobs < max_consecutive_jobs:
        return wait
    else:
        Publisher_profile['Status'] = 'Completed'
        return workdone
if __name__ == '__main__':
    app.run(debug=True, port=5001)