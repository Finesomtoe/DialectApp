"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from DialectApp import app

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

@app.route('/contact')
def contact():
    return render_template('contact.html')
