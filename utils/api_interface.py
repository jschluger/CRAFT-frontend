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
    args = {'k': k}
    if t is not None:
        args['t'] = t
    r = requests.post(data.BACKEND+'/viewtop', data=args)
    return r.json()

def get_ranks_formatted(k, t):
    rank_json = get_ranks(k,t)
    # print(f'requesting ranks returned {rank_json}')
    this_time = format_time(rank_json['when'])
    # print(rank_json['ranking'][0][1].split('/'))
    if rank_json['ranking'] == None:
        franks = []
    else:
        franks = rank_json['ranking']
    return this_time, franks

def get_times():
    r = requests.post(data.BACKEND+'/viewtimes')
    return r.json()    

def get_convo(i):
    args = {'id': i}
    # print(f'making backend request for convo {i}')
    r = requests.post(data.BACKEND+'/viewconvo', data=args)
    # print('recieved response')
    return r.json()
    
