from flask import render_template, redirect, url_for
from flask.ext.login import login_user
from . import main
from .forms import SignupForm
from .. import db, lm
from ..models import Student

@lm.user_loader
def load_user(id):
   return Student.query.filter_by(id=int(id)).first()


@main.route('/', methods=["GET", "POST"])
def index():
	form = SignupForm()
	stud = None

	if form.validate_on_submit():
		student = Student(
			name=form.name.data,
			password=form.password.data
		)
		db.session.add(student)
		db.session.commit()
		login_user(student)
		stud = student
		return redirect(url_for('.index'))

	return render_template('index.html', form=form, student=stud)