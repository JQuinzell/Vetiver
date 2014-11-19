from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, login_required, logout_user
from . import main
from .forms import SignupForm, LoginForm
from .. import db, lm
from ..models import Student

@main.route('/', methods=["GET", "POST"])
def index():
	form = SignupForm()
	login = LoginForm()

	if form.validate_on_submit():
		student = Student(
			name = form.name.data,
			password = form.password.data
			)
		db.session.add(student)
		db.session.commit()
		login_user(student)
		flash("You have signed up")
		return redirect(url_for('.index'))

	return render_template('index.html', form=form, login=login)