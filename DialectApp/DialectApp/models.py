
from DialectApp import app, mysql, db, login_manager 
from werkzeug import generate_password_hash, check_password_hash
from datetime import datetime 
from flask.ext.login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    """description of class"""
    __tablename__ = 'user_test'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique = True)
    username = db.Column(db.String(100))
    pwdhash = db.Column(db.String(100))
    region = db.Column(db.String(120))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)

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

    #def generate_confirmation_token(self, expiration=3600):
    #    s = Serializer(app.config['SECRET_KEY'], expiration)
    #    return s.dumps({'confirm': self.id})

    #def confirm(self, token):
    #    s = Serializer(app.config['SECRET_KEY'])
    #    try:
    #        data = s.loads(token)
    #    except:
    #        return False
    #    if data.get('confirm') != self.id:
    #        return False
    #    self.confirmed = True
    #    db.session.add(self)
    #    return True


