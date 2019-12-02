from flask import Blueprint, request, render_template
import time, json, data
from utils import api_interface

routes = Blueprint('routes', __name__)

@routes.route("/")
@routes.route("/<time>")
def home(time=None):
    """
    home
    """
    ftimes = api_interface.get_times_formatted()
    this_time, franks = api_interface.get_ranks_formatted(time)
    return render_template('index.html',
                           backend=data.BACKEND,
                           times=ftimes,
                           ranks=franks,
                           this_time=this_time,
                           k=data.k)


