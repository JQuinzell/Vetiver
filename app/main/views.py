from flask import render_template, redirect, url_for
from flask.ext.login import login_user, login_required, logout_user
from . import main
from .forms import SignupForm, LoginForm
from .. import db, lm
from ..models import Student

@lm.user_loader
def load_user(id):
   return Student.query.filter_by(id=int(id)).first()


@main.route('/', methods=["GET", "POST"])
def index():
	form = SignupForm()
	login = LoginForm()

	if form.validate_on_submit():
		student = Student(
			name=form.name.data,
			password=form.password.data
		)
		db.session.add(student)
		db.session.commit()
		login_user(student)
		return redirect(url_for('.index'))

	if login.validate_on_submit():
		student = Student.query.filter_by(name=login.name.data).first()
		if student is not None and student.verify_password(login.password.data):
			login_user(student)
			return redirect(url_for('.index'))

	return render_template('index.html', form=form, login=login)

@login_required
@main.route('/secret')
def secret():
	return "<h1>GOOD JOB</h1>"

@login_required
@main.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.index'))