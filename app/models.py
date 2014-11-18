from . import db

class Student(db.Model):
	__tablename__ = 'students'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))
	rankings = db.relationship('Ranking', backref='student')
	password = db.Column(db.String(80)) # Need to use hashing
	points = db.Column(db.Integer, default=0)
	spells = db.relationship('Spell', backref='caster')
	posts = db.relationship('Post', backref='student')

	def is_active(self):
		return True

	def get_id(self):
		return unicode(self.id)

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True

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