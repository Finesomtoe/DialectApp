"""
This script runs the DialectApp application using a development server.
"""

from os import environ
from DialectApp import app

if __name__ == '__main__':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(environ.get('SERVER_PORT', '2424'))
    #except ValueError:
    #    PORT = 2424
    app.run(host='localhost', port=2424)
