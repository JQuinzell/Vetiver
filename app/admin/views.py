from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, login_required, logout_user, current_user
from . import admin
from .forms import RoomForm
from .. import db
from ..models import Room

@admin.before_request
def authenticate_admin():
	if(not current_user.is_authenticated() or not current_user.admin):
		return redirect(url_for('main.index'))

@admin.route('/')
def index():
	rooms = Room.query.all()
	return render_template('admin/index.html', rooms=rooms)

@admin.route('/create-room', methods=['GET', 'POST'])
def create_room():
	form = RoomForm()

	if form.validate_on_submit():
		room = Room(
			name=form.name.data,
			description=form.description.data
		)
		db.session.add(room)
		db.session.commit()
		flash("%s room has been created!" % room.name)
		return redirect(url_for('admin.index'))

	return render_template('admin/new-room.html', form=form)