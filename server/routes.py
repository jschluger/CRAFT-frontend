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

    ftimes = api_interface.get_times_formatted()
    this_time, franks = api_interface.get_ranks_formatted(k, t)
    return render_template('home.html',
                           backend=data.BACKEND,
                           times=ftimes,
                           ranks=franks,
                           this_time=this_time,
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
        
    conv, parent, children = api_interface.get_convo_formatted(i)
    return render_template('convo.html',
                           convo=conv,
                           parent=parent,
                           children=children,
                           id=i)


@routes.route("/about")
def about():
    """
    The about this project page. 
    """
    return render_template('about.html')
