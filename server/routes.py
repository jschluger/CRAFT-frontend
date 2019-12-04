from flask import Blueprint, request, render_template
import time, json, data
from utils import api_interface

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    """
    home
    """
    t=None
    try:
        if 't' in request.args:
            t = int(request.args['t'])
    except Exception as e:
        print(f'got exception <{e}> while parsing arg t')
    k = data.k
    try:
        if 'k' in request.args:
            k = request.args['k']
    except Exception as e:
        print(f'got exception <{e}> while parsing arg k')

    ftimes = api_interface.get_times_formatted()
    this_time, franks = api_interface.get_ranks_formatted(k, t)
    return render_template('home.html',
                           backend=data.BACKEND,
                           times=ftimes,
                           ranks=franks,
                           this_time=this_time,
                           k=k)


@routes.route("/about")
def about():
    return render_template('about.html')
