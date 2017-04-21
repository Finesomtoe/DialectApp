"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, session, url_for, flash 
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Email, ValidationError
from flask import request
from flask import redirect 
from DialectApp import app, mysql, db

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required("Name is required.")])
    email = StringField('Email', validators=[Email("Email is required")])
    comment = TextAreaField('Enter your comment', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'home.html',
        title = 'Home Page',
        year = datetime.now().year,)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', title = 'Flasky', name=name)

@app.route('/redirect')
def redirectme():
    return redirect('http://www.google.com')

@app.route("/authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from user_test where username='" + username + "' and password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    name = None;
    email = None;
    comment = None;
    form = NameForm();
    if form.validate_on_submit():
        session['name'] = form.name.data
        form.name.data = ''     
        email = form.email.data
        form.email.data = ''
        comment = form.comment.data
        form.comment.data = ''
        flash("Thank you for submitting your question. We'll get back to you as soon as possible!")
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form, name=session.get('name'), email=email, comment=comment)

@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'