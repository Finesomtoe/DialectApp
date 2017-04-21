
from DialectApp import app, mysql, db 
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
    """description of class"""
    __tablename__ = 'user_test'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique = True)
    username = db.Column(db.String(100))
    pwdhash = db.Column(db.String(100))
    region = db.Column(db.String(120))

