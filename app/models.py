from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

class Student(UserMixin, db.Model):
	__tablename__ = 'students'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))
	rankings = db.relationship('Ranking', backref='student')
	admin = db.Column(db.Boolean, default=False)
	password_hash = db.Column(db.String(128))
	points = db.Column(db.Integer, default=0)
	spells = db.relationship('Spell', backref='caster')
	posts = db.relationship('Post', backref='student')

	@property
	def password(self):
		raise AttributeError('password is not readable')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def add_points(self, num):
		self.points += num

	def deduct_points(self, num):
		self.points -= num

class Spell(db.Model):
	__tablename__ = 'spells'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))
	student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
	cost = db.Column(db.Integer)
	description = db.Column(db.Text)

class Rank(db.Model):
	__tablename__ = 'ranks'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60))
	cost = db.Column(db.Integer)

class Tree(db.Model):
	__tablename__ = 'trees'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60))
	description = db.Column(db.Text)

class Ranking(db.Model):
	__tablename__ = 'rankings'

	rank_id = db.Column(db.Integer, db.ForeignKey('ranks.id'), primary_key=True)
	tree_id = db.Column(db.Integer, db.ForeignKey('trees.id'), primary_key=True)
	rank = db.relationship('Rank', backref='rankings')
	tree = db.relationship('Tree', backref='rankings')
	student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

	def title(self):
		return self.rank.name + ' - ' + self.tree.name

post_tags = db.Table('post_tags',
	db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
	db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)

class Post(db.Model):
	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('students.id'))
	body = db.Column(db.Text)
	created_at = db.Column(db.DateTime)
	tags = db.relationship('Tag', secondary=post_tags, backref="posts")

class Tag(db.Model):
	__tablename__ = 'tags'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))