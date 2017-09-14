#libraries 
from flask import Flask, render_template, flash, url_for, session, logging, redirect, request
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt

from forms.login import LoginForm
from forms.signup import SignupForm

app = Flask(__name__)
app.secret_key = '$5$rounds=535000$O/od5B7GUkTCkcG.$7U6jJ6QnLvyJo8NkAch7KWfwMrPKolfzwtYJOq/7JQ5'
app.debug = True


#Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errorpages/404.html')


# App home page
# Show feed if logged in else show them a page to login or signup

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')
	pass

@app.route('/login')
def login():
	form = LoginForm(request.form)
	return render_template('login.html', form=form)
	pass

@app.route('/signup')
def signup():
	form = SignupForm(request.form)
	return render_template('signup.html', form=form)
	pass

@app.route('/logout')
def logout():
	session.clear()
	flash('You are now logged out', 'success')
	return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()