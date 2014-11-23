from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, login_required, logout_user, current_user
from . import profile
# from .forms import RoomForm, TagForm, PointForm
from .. import db
from ..models import Room, Tag, Post, Student

@profile.before_request
def require_login():
	if not current_user.is_authenticated():
		return redirect(url_for('main.index'))

@profile.route('/profile/<name>')
def index(name):
	student = Student.query.filter_by(name=name).first_or_404()
	return render_template('/profile/index.html', student=student)


