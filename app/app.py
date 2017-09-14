#libraries 
from flask import Flask, render_template, flash, url_for, session, logging, redirect, request
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt

from forms.login import LoginForm
from forms.signup import SignupForm

from helpers.decorators import login_required

app = Flask(__name__)
app.config.from_pyfile('config.py')
# init MYSQL
mysql = MySQL(app)


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

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)

	if request.method == 'POST' and form.validate():
		username = form.username.data
		password = form.password.data
		cur = mysql.connection.cursor()
		result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
		if result > 0:
			data = cur.fetchone()
			db_password = data['password']
			if sha256_crypt.verify(password, db_password):
				session['logged_in'] = True
				session['username'] = username

				flash('You are now loggedin', 'success')
				return redirect(url_for('index'))
			else:
				flash('Your password is incorrect', 'danger')
		else:
			flash('No user found with these details', 'danger')		
	return render_template('login.html', form = form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm(request.form)

	if request.method == 'POST' and form.validate():
		name = form.name.data
		email = form.email.data
		username = form.username.data
		password = sha256_crypt.encrypt(str(form.password.data))
		
		# mysql connection

		cur = mysql.connection.cursor()

		cur.execute("INSERT INTO users(name, email, username, password) values(%s, %s, %s, %s)",(name, email, username, password))
		mysql.connection.commit()
		cur.close()

		flash('You are now registered', 'success')
		return redirect(url_for('login'))
	return render_template('signup.html', form = form)

@app.route('/logout')
def logout():
	session.clear()
	flash('You are now logged out', 'success')
	return redirect(url_for('login'))


@app.route('/profile')
@login_required
def profile():
	return render_template('profile.html')
	pass

@app.route('/settings')
@login_required
def settings():
	return render_template('settings.html')
	pass

if __name__ == '__main__':
    app.run()