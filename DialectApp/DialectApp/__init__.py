"""
The flask application package.
"""

from flask import Flask
from flask import render_template
from flask.ext.mysql import MySQL
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import Mail, Message
from threading import Thread
from flask.ext.moment import Moment



mysql = MySQL()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.signin'
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'somtoskeyinwhichnobodycanguess'
app.config["MAIL_SERVER"] = "smtp.mail.yahoo.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'senendu5@yahoo.com'
app.config["MAIL_PASSWORD"] = 'somteechinaza95'
app.config['DIALECT_APP_SUBJECT'] = '[Dialect App]'
app.config['DIALECT_APP_SENDER'] = 'senendu5@yahoo.com'
#app.config['SECRET_KEY'] = 'my very secret yeeeys'
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'sokoamshe619+'
#app.config['MYSQL_DATABASE_DB'] = 'testdb'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)
login_manager.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://limdialect_admin:OeOCMPSMn8NT7@mysql-limdialect.science.ru.nl/limdialect'
db = SQLAlchemy(app)
mail = Mail(app)
moment = Moment(app)
   
def send_async_email(app, msg):
      with app.app_context():
          mail.send(msg)

def send_email(to, subject, template, **kwargs):
      msg = Message(app.config['DIALECT_APP_SUBJECT'] + subject,
                    sender=app.config['DIALECT_APP_SENDER'], recipients=[to])
      msg.body = render_template(template + '.txt', **kwargs)
      #msg.html = render_template(template + '.html', **kwargs)
      thr = Thread(target=send_async_email, args=[app, msg])
      thr.start()
      return thr 

import DialectApp.views
 

