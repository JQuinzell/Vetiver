from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, ValidationError, TextAreaField, IntegerField
from wtforms.validators import Required, Length, EqualTo, Regexp
from ..models import Room, Tag


class RoomForm(Form):
	name = StringField("Room Name", validators=[Required()])
	description = TextAreaField("Room Description")
	submit = SubmitField("Submit")

	def validate_name(self, field):
		if Room.query.filter_by(name=field.data).first():
			raise ValidationError("Name has already been taken!")

class TagForm(Form):
	name = StringField("Tag Name", validators=[Required()])
	submit = SubmitField("Submit")

	def validate_name(self, field):
		if Tag.query.filter_by(name=field.data).first():
			raise ValidationError("Name has already been taken!")

class PointForm(Form):
	points = IntegerField("Points")
	submit = SubmitField("Submit")