from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, login_required, logout_user, current_user
from . import admin
# from .forms import LoginForm
from .. import db
from ..models import Tag

@admin.before_request
def authenticate_admin():
	if(not current_user.is_authenticated() or not current_user.admin):
		return redirect(url_for('main.index'))

@admin.route('/')
def index():
	return render_template('admin/index.html')