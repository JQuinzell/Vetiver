from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, login_required, logout_user, current_user
from . import admin
from .forms import RoomForm, TagForm
from .. import db
from ..models import Room, Tag, Post

@admin.before_request
def authenticate_admin():
	if(not current_user.is_authenticated() or not current_user.admin):
		return redirect(url_for('main.index'))

@admin.route('/')
def index():
	rooms = Room.query.all()
	tags = Tag.query.all()

	return render_template('admin/index.html', rooms=rooms, tags=tags)

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

@admin.route('/create-tag', methods=['GET', 'POST'])
def create_tag():
	form = TagForm()

	if form.validate_on_submit():
		tag = Tag(name=form.name.data)
		db.session.add(tag)
		db.session.commit()
		flash("%s tag has been created!" % tag.name)
		return redirect(url_for('admin.index'))

	return render_template('admin/new-tag.html', form=form)

@admin.route('/posts')
def posts():
	posts = Post.query.filter(Post.closed == False).all()
	return render_template('admin/posts.html', posts=posts)

@admin.route('/posts/<int:id>/close')
def close_post(id):
	post = Post.query.get_or_404(id)
	post.closed = True
	db.session.add(post)
	db.session.commit()
	return redirect(url_for('admin.posts'))