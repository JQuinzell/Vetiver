from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import Required, Length, EqualTo, Regexp
from ..models import Room


class RoomForm(Form):
	name = StringField("Tag Name", validators=[Required()])
	description = TextAreaField("Room Description")
	submit = SubmitField("Submit")

	def validate_name(self, field):
		if Room.query.filter_by(name=field.data).first():
			raise ValidationError("Name has already been taken!")
