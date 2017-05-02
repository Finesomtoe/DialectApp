"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, session, url_for, flash  
from flask import request
from flask import redirect 
from DialectApp import app, mysql, db, send_email, mail 
from .forms import ContactForm, SignupForm, SigninForm, EditProfileForm
from .models import User
from flask.ext.login import login_user, logout_user, login_required
from flask.ext.mail import Message



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

@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
  
  if 'email' in session:
    return redirect(url_for('profile')) 

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.email.data, form.username.data, form.password.data, form.region.data)
      db.session.add(newuser)
      db.session.commit()
      #msg = Message('Welcome to Dialect App', sender='senendu5@yahoo.com', recipients=[newuser.email])
      #msg.body = 'Dear ' + newuser.username.title() + ',' + '\n\nWelcome to the Dialect App! You are now registered in our application. Enjoy pronouncing. \n\nSincerely, \nThe Dialect App Team'
      #mail.send(msg)
      #token = newuser.generate_confirmation_token()
      send_email(newuser.email, 'Welcome to Dialect App', 'confirm', newuser=newuser)
      #session['email'] = newuser.email
      login_user(newuser)
      return redirect(url_for('profile', username=newuser.username))  

  elif request.method == 'GET':
    return render_template('signup.html', form=form)

@app.route('/sign_in', methods=['GET', 'POST'])
def signin():
  form = SigninForm()
   
  if 'email' in session:
    return redirect(url_for('profile')) 

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
        user = User.query.filter_by(email=form.email.data).first()
        #session['email'] = form.email.data
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('profile', username=user.username))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)

@app.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        return redirect('http://www.google.com')
    else:
        return render_template('profile.html', user=user)
  

@app.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('home'))
 
  #if 'email' not in session:
    #return redirect(url_for('auth.signin'))
     
  #session.pop('email', None)


@app.route('edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
         current_user.username = form.username.data
         current_user.about_me = form.about_me.data
         db.session.commit()
         return redirect(url_for('profile', username=current_user.username))
    form.username.data = current_user.username
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form) 