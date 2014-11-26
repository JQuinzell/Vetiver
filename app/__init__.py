from flask import Flask
import psycopg2
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config

db = SQLAlchemy()
lm = LoginManager()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	db.init_app(app)
	lm.init_app(app)

	from .main import main as main_blueprint
	from .auth import auth as auth_blueprint
	from .admin import admin as admin_blueprint
	from .profile import profile as profile_blueprint
	app.register_blueprint(main_blueprint)
	app.register_blueprint(auth_blueprint)
	app.register_blueprint(profile_blueprint)
	app.register_blueprint(admin_blueprint, url_prefix="/admin")
	
	return app