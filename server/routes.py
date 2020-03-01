from flask import Blueprint, request, render_template, abort
import time, json, data
from utils import api_interface

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    """
    Display Rankings, and way to request rankings produced at other times. 
    """
    t=None
    try:
        if 't' in request.args:
            t = int(request.args['t'])
    except Exception as e:
        print(f'got exception <{e}> while parsing arg t in /')
    k = data.k
    try:
        if 'k' in request.args:
            k = int(request.args['k'])
    except Exception as e:
        print(f'got exception <{e}> while parsing arg k in /')

    times = api_interface.get_times()
    ranks = api_interface.get_ranks(k, t)
    
    if 'internal_error' in times or 'internal_error' in ranks:
        abort(500)
    
    return render_template('home.html',
                           backend=data.BACKEND,
                           times=times['times'][::-1],
                           ranks=ranks['ranking'],
                           this_time=ranks['when'],
                           distrib=ranks['distrib'],
                           duration=ranks['duration'],
                           k=k)


@routes.route("/convo")
def convo():
    """
    Display convo
    """
    # print('requesting /convo')
    i=None
    try:
        if 'id' in request.args:
            i = request.args['id']
    except Exception as e:
        print(f'got exception <{e}> while parsing arg id in /convo')
    # print(f'\twith id={i}')
        
    convo = api_interface.get_convo(i)
    if 'internal_error' in convo:
        abort(500)
    for c in convo['convo']:
        c[3] = c[3].split('\n')
    
    return render_template('convo.html',
                           convo=convo['convo'],
                           parent=convo['parent'],
                           endings=convo['endings'],
                           id=convo['id'],
                           post_name=convo['post_name'],
                           post_author=convo['post_author'],
                           score_pos=1)


@routes.errorhandler(500)
def err(e):
    return render_template('error.html')


@routes.route("/about")
def about():
    """
    The about this project page. 
    """
    return render_template('about.html')

@routes.context_processor
def base_data():
    return dict(craft_thresh=0.548580,
                arrow_thresh=.2,
                format_time=api_interface.format_time,
                format_duration=api_interface.format_duration)

