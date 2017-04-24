"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, session, url_for, flash 
from flask import request
from flask import redirect 
from DialectApp import app, mysql, db
from .forms import SignupForm, ContactForm
from .models import User


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
    form = ContactForm();
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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.email.data, form.username.data, form.password.data, form.region.data)
      db.session.add(newuser)
      db.session.commit()
      session['email'] = newuser.email
      return redirect(url_for('profile'))  

  elif request.method == 'GET':
    return render_template('signup.html', form=form)

@app.route('/profile')
def profile():
 
  if 'email' not in session:
    return redirect('http://www.google.com')
 
  user = User.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect('http://www.google.com')
  else:
    return render_template('profile.html')