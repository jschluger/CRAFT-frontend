from gevent import monkey
monkey.patch_all()

import data
from server import app

# parse command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--dev', default=False, action='store_true',
    help='Configure the ip address of the backend for development.')
args = parser.parse_args()
if args.dev:
    data.BACKEND = 'http://0.0.0.0:8080'

from gevent import pywsgi

# data.args = args

print(__name__)
if __name__ == '__main__':
    # start the flask app! 
    # app.run(host='0.0.0.0', port=8081, use_reloader=True)
    server = pywsgi.WSGIServer(listener=('0.0.0.0', 8081), application=app)
    print('Starting server!')
    server.serve_forever()
