from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, PasswordField, ValidationError
from wtforms.validators import Required, Length, EqualTo, Regexp
from ..models import Student, Tag
from ..auth.forms import LoginForm

class SignupForm(Form):
	name = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
	password = PasswordField("New Password", validators=[Required(), EqualTo('confirm', message="Passwords must match")])
	confirm = PasswordField("Confirm Password")
	submit = SubmitField("Submit")

	def validate_name(self, field):
		if Student.query.filter_by(name=field.data).first():
			raise ValidationError("Name has already been taken")

class ProfileForm(Form):
	name = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
	submit = SubmitField("Submit")

	def validate_name(self, field):
		if Student.query.filter_by(name=field.data).first():
			raise ValidationError("Name has already been taken")

class PostForm(Form):
	body = TextAreaField(validators=[Required()])
	tag = SelectField('Tag', coerce=int)
	submit = SubmitField("Post")

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.tag.choices = [(tag.id, tag.name) for tag in Tag.query.all()]
		self.tag.choices.insert(0, (0, '--select tag--'))