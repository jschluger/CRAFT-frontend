from gevent import monkey
monkey.patch_all()

import data
from server import app

# parse command line arguments
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--backend', default='http://0.0.0.0:8080',
#     help='The full address and port of the CRAFT_backend server')
# args = parser.parse_args()
# data.BACKEND = args.backend

from gevent import pywsgi

# data.args = args

print(__name__)
if __name__ == '__main__':
    # start the flask app! 
    # app.run(host='0.0.0.0', port=8081, use_reloader=True)
    server = pywsgi.WSGIServer(listener=('0.0.0.0', 8081), application=app)
    print('Starting server!')
    server.serve_forever()
