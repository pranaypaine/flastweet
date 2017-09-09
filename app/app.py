#libraries 
from flask import Flask, render_template, flash, url_for, session, logging, redirect, request
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = '$5$rounds=535000$O/od5B7GUkTCkcG.$7U6jJ6QnLvyJo8NkAch7KWfwMrPKolfzwtYJOq/7JQ5'
app.debug = True


#Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errorpages/404.html')


#Main app
@app.route('/')
def index():
	return render_template('index.html')
	pass


if __name__ == '__main__':
    app.run()