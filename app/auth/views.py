from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, login_required, logout_user
from . import auth
from .forms import LoginForm
from .. import db, lm
from ..models import Student

@lm.user_loader
def load_user(id):
   return Student.query.filter_by(id=int(id)).first()


@auth.route('/login', methods=["POST"])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		student = Student.query.filter_by(name=form.name.data).first()
		if student is not None and student.verify_password(form.password.data):
			login_user(student)
			flash("You have logged in")
			return redirect(url_for('main.index'))

	flash("Incorrect name or password")
	return redirect(url_for('main.index'))

@login_required
@auth.route('/logout') # Not using post as to avoid using a form for a link for now
def logout():
	logout_user()
	flash("You have been logged out")
	return redirect(url_for('main.index'))