"""
The flask application package.
"""

from flask import Flask
from flask.ext.mysql import MySQL
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


mysql = MySQL()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.signin'
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'somtoskeyinwhichnobodycanguess'
#app.config['SECRET_KEY'] = 'my very secret yeeeys'
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'sokoamshe619+'
#app.config['MYSQL_DATABASE_DB'] = 'testdb'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)
login_manager.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sokoamshe619+@localhost/testdb'
db = SQLAlchemy(app)
   

import DialectApp.views
 

