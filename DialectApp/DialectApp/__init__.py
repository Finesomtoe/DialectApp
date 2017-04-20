"""
The flask application package.
"""

from flask import Flask
from flask.ext.mysql import MySQL
from flask.ext.bootstrap import Bootstrap

mysql = MySQL()
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'my very secret yeeeys'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sokoamshe619+'
app.config['MYSQL_DATABASE_DB'] = 'testdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

import DialectApp.views