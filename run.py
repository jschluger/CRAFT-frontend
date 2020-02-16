# # parse command line arguments
# import argparse
# parser = argparse.ArgumentParser()
# args = parser.parse_args()

from gevent import monkey
monkey.patch_all()

from server import app
import data

from gevent import pywsgi

# data.args = args

if __name__ == '__main__':
    # start the flask app!
    # app.run(host='0.0.0.0', port=8081, use_reloader=True)

    server = pywsgi.WSGIServer(listener=('0.0.0.0', 8081), application=app)
    print('Starting server!')
    server.serve_forever()
