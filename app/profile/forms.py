from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, PasswordField, ValidationError
from wtforms.validators import Required, Length, EqualTo, Regexp

class RequestForm(Form):
	name = StringField('Name', validators=[Required()])
	description = TextAreaField('Description', validators=[Required(), Length(min=20)])
	submit = SubmitField('Submit')
