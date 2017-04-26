from flask.ext.wtf import Form
from .models import User
from DialectApp import db
from wtforms import StringField, TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField, BooleanField

class SignupForm(Form):
  username = TextField("User name",  [validators.Required("Please enter a username."), validators.Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')], render_kw={"placeholder": "Username"})
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")], render_kw={"placeholder": "Email Address"})
  password = PasswordField('Password', [validators.Required("Please enter a password."), validators.EqualTo('password2', message='Passwords must match.')], render_kw={"placeholder": "Password"})
  password2 = PasswordField('Confirm password', [validators.Required("Confirm your password")], render_kw={"placeholder": "Confirm Password"})
  region = TextField("Region",  [validators.Required("Please enter your region of origin.")], render_kw={"placeholder": "Region"})
  submit = SubmitField("Create account")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    nameofuser = User.query.filter_by(username = self.username.data.lower()).first()
    if user:
      self.email.errors.append("That email is already registered")
      return False
    elif nameofuser:
        self.username.errors.append("Username already in use ")
        return False
    else:
      return True

class SigninForm(Form):
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")], render_kw={"placeholder": "Email Address"})
  password = PasswordField('Password', [validators.Required("Please enter a password.")], render_kw={"placeholder": "Password"})
  remember_me = BooleanField('Keep me logged in')
  submit = SubmitField("Sign In")
   
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.email.errors.append("Invalid e-mail or password")
      return False

class ContactForm(Form):
    name = StringField('What is your name?', [validators.Required("Name is required.")])
    email = StringField('Email', [validators.Email("Email is required")])
    comment = TextAreaField('Enter your comment', [validators.Required("Write your comment")])
    submit = SubmitField('Submit')
