
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

    def __init__(self, email, username, password, region):      
        self.email = email.lower()
        self.username = username.lower()  
        self.set_password(password)
        self.region = region.title()
     
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    def __repr__(self):
        return '<User %r>' % self.username

