from flask import Blueprint, request, render_template
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

    return render_template('home.html',
                           backend=data.BACKEND,
                           times=times['times'][::-1],
                           ranks=ranks['ranking'],
                           this_time=ranks['when'],
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
    return render_template('convo.html',
                           convo=convo['convo'],
                           parent=convo['parent'],
                           children=convo['children'],
                           id=convo['id'],
                           post_name=convo['post_name'],
                           post_author=convo['post_author'])


@routes.route("/about")
def about():
    """
    The about this project page. 
    """
    return render_template('about.html')

@routes.context_processor
def base_data():
    return dict(craft_thresh=0.548580, arrow_thresh=.2, format_time=api_interface.format_time)
