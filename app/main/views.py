from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_required, current_user, login_user
from . import main
from .forms import SignupForm, LoginForm, ProfileForm
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

@login_required
@main.route('/profile/edit', methods=["GET", "POST"])
def edit():
	form = ProfileForm()

	if form.validate_on_submit():
		current_user.name = form.name.data
		db.session.add(current_user)
		db.session.commit()
		flash("Profile updated")
		return redirect(url_for('main.index'))

	form.name.data = current_user.name

	return render_template('user/edit.html', form=form)