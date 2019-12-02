from flask import Blueprint, request, render_template
import time, json, data


routes = Blueprint('routes', __name__)

@routes.route("/", methods=['GET'])
def home():
    """
    home
    """
    return render_template('index.html',backend=data.BACKEND)


