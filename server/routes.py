from flask import Blueprint, request, render_template, abort, make_response
import time, json, data
from utils import api_interface
from pprint import pprint

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
        
    update_score_pos=None
    try:
        if 'update_score_pos' in request.args:
            update_score_pos = int(request.args['update_score_pos'])
    except Exception as e:
        print(f'got exception <{e}> while parsing arg update_score_pos in /convo')
        
    convo = api_interface.get_convo(i)
    if 'internal_error' in convo:
        abort(500)
    for c in convo['convo']:
        c['text'] = c['text'].split('\n')


    score_pos = 1 # initalize to interstitial display if cookie is not set
    if update_score_pos != None:
        score_pos = update_score_pos
    elif 'score_pos' in request.cookies:
        score_pos = int(request.cookies['score_pos'])
        
    # assert type(score_pos)==int
    # print(f'rendering convo with score_pos={score_pos}')

    # If displaying next to prediction, need to shift scores down a row because backend sends scores
    # associated with last comment in the context. 
    if score_pos == 0:
        for idx in range(1, len(convo['convo']))[::-1]:
            convo['convo'][idx]['score'] = convo['convo'][idx-1]['score']
        if len(convo['convo']) > 0:
               convo['convo'][0]['score'] = 0
    
    resp = make_response( render_template('convo.html',
                                          convo=convo['convo'],
                                          parent=convo['parent'],
                                          endings=convo['endings'],
                                          id=convo['id'],
                                          convo_name=convo['convo_name'],
                                          post_author=convo['post_author'],
                                          score_pos=score_pos) )
    
    # print(f'cookies was {request.cookies}')
    if update_score_pos != None or 'score_pos' not in request.cookies:
        resp.set_cookie('score_pos', str(score_pos))
    return resp

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
                format_duration=api_interface.format_duration,
                still_active=api_interface.still_active,
                now=time.time(),
                derail=" become toxic")

