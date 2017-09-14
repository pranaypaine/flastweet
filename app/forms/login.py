from wtforms import *

class LoginForm(Form):
	"""docstring for LoginForm"""
	username = StringField('username')
	password = PasswordField('password')