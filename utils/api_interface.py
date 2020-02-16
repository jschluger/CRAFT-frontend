import requests, data, time
from datetime import datetime
from pprint import pprint

def format_time(t):
    if type(t) != int and type(t) != float:
        return t
    elif t==-1:
        return "Live"
    else:
        return datetime.utcfromtimestamp(t).strftime("%I:%M:%S %p on %b %-d, %Y UTC")

def get_ranks(k,t):
    r = {'internal_error': True} # default
    args = {'k': k}
    if t is not None:
        args['t'] = t
    try:
        r = requests.post(data.BACKEND+'/viewtop', data=args, timeout=1)
    except requests.exceptions.ConnectionError as e:
        print(f'\nfailed to request {data.BACKEND}/viewtop\n\tgot exception {e}')
        return 
    return r if type(r)==dict else r.json()

def get_times():
    r = {'internal_error': True} # default
    try:
        r = requests.post(data.BACKEND+'/viewtimes', timeout=1)
    except requests.exceptions.ConnectionError as e:
        print(f'\nfailed to request {data.BACKEND}/viewtimes\n\tgot exception {e}')
    return r if type(r)==dict else r.json()    

def get_convo(i):
    r = {'internal_error': True} # default
    args = {'id': i}
    try:
        r = requests.post(data.BACKEND+'/viewconvo', data=args, timeout=1)
    except requests.exceptions.ConnectionError as e:
        print(f'\nfailed to request {data.BACKEND}/viewconvo\n\tgot exception {e}')
    return r if type(r)==dict else r.json()
    
