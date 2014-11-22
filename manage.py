import os
from app import create_app, db
# import models
from app.models import Student, Post, Tag
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
	# set any variables you want in the shell
	return dict(app=app, db=db, Student=Student, Post=Post, Tag=Tag)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
	# runs test suite
	import unittest
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
	manager.run()