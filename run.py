# parse command line arguments
import argparse
parser = argparse.ArgumentParser()
args = parser.parse_args()

from server import app
import data

data.args = args

if __name__ == '__main__':
    # start the flask app!
    app.run(host='0.0.0.0', port=8081, use_reloader=False)
    
