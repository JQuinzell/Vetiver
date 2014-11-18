from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, PasswordField
from wtforms.validators import Required, Length, EqualTo

class SignupForm(Form):
	name = StringField("Your name, nigga", validators=[Required()])
	password = PasswordField("New Password", [Required(), EqualTo('confirm')])
	confirm = PasswordField("Confirm Password")
	submit = SubmitField("Submit")

