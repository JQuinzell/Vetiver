from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(Form):
	name = StringField()
	password = PasswordField()
	submit = SubmitField()