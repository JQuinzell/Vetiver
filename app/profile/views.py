from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, login_required, logout_user, current_user
from . import profile
from .forms import RequestForm
from .. import db
from ..models import Room, Tag, Post, Student, Spell

@profile.before_request
def require_login():
	if not current_user.is_authenticated():
		return redirect(url_for('main.index'))

@profile.route('/profile/<name>', methods=['GET', 'POST'])
def index(name):
	student = Student.query.filter_by(name=name).first_or_404()
	form = RequestForm()
	if form.validate_on_submit():
		spell = Spell(name=form.name.data, description=form.description.data, caster=student)
		db.session.add(spell)
		db.session.commit()
		print "Validated!"
		print spell
		flash("Spell request made!")
		return redirect(url_for('profile.index', name=student.name))
	return render_template('/profile/index.html', student=student, form=form)