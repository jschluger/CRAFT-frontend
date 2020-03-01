import requests, data, time
from datetime import datetime
from pprint import pprint

def format_time(t):
    if type(t) != int and type(t) != float:
        return t
    elif t==-1:
        return "Live"
    else:
        return datetime.utcfromtimestamp(t).strftime("%I:%M %p; %b %-d, %Y UTC")

def format_duration(t):
    if type(t) != int and type(t) != float:
        return t
    t = int(t)
    s = ''
    if t >= data.SEC_PER_DAY:
        n = t // data.SEC_PER_DAY
        s += f'{n} Day{"s" if n > 1 else ""} '
        t %= data.SEC_PER_DAY
        
    if t >= data.SEC_PER_HOUR:
        n = t // data.SEC_PER_HOUR
        s += f'{n} Hour{"s" if n > 1 else ""} '
        t %= data.SEC_PER_HOUR
        
    if t >= 60:
        n = t // 60
        s += f'{n} Minute{"s" if n > 1 else ""}'

    return s

    
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
    
