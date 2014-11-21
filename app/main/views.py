from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_required, current_user, login_user
from . import main
from .forms import SignupForm, LoginForm, ProfileForm, PostForm
from .. import db, lm
from ..models import Student, Room, Post

@main.route('/', methods=["GET", "POST"])
def index():
	form = SignupForm()
	login = LoginForm()
	rooms = Room.query.all()

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

	return render_template('index.html', form=form, login=login, rooms=rooms)

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

@login_required
@main.route('/rooms/<name>', methods=['GET', 'POST'])
def room(name):
	form = PostForm()
	room = Room.query.filter_by(name=name).first()
	posts = room.posts

	if form.validate_on_submit():
		post = Post(student=current_user, body=form.body.data)
		room.posts.append(post)
		flash("Posted Successfully!!!!")
		db.session.add(post)
		db.session.commit()
		print post.created_at
		return redirect(url_for('main.room', name=room.name))



	return render_template('room.html', room=room, form=form, posts=posts)