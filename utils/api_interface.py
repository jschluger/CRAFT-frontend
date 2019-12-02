import requests, data, time
from datetime import datetime
from pprint import pprint

def get_ranks(time=None):
    args = {'k': data.k}
    if time is not None:
        args['t'] = time
    r = requests.post(data.BACKEND+'/viewtop', data=args)
    return r.json()

def get_ranks_formatted(time=None):
    rank_json = get_ranks(time=time)
    this_time = f'{datetime.utcfromtimestamp(rank_json["when"]).strftime("%Y-%m-%d %H:%M:%S")} UTC'
    # print(rank_json['ranking'][0][1].split('/'))
    franks = list(map(lambda t: # t = (score, link)
                      (t[0], t[1], "/".join(t[1].split("/")[-3:])),
                      rank_json['ranking'] ))
    return this_time, franks

def get_times():
    r = requests.post(data.BACKEND+'/viewtimes')
    return r.json()

def get_times_formatted():
    times = get_times()['times']
    formatted = list(map(lambda t: (t, f'{datetime.utcfromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")} UTC'), times))

    return formatted
    
