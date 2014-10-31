from . import db

class Rankable(db.Model):
	__tablename__ = 'rankables'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))
	type = db.Column(db.String(40))
	rankings = db.relationship('Ranking', backref='rankable')

	__mapper_args__ = {
		'polymorphic_identity': 'rankable',
		'polymorphic_on': type,
	}

student_spells = db.Table('student_spells',
	db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
	db.Column('spell_id', db.Integer, db.ForeignKey('spells.id'))
)

class Student(Rankable):
	__tablename__ = 'students'

	id = db.Column(db.Integer, db.ForeignKey('rankables.id'), primary_key=True)
	points = db.Column(db.Integer, default=0)
	spells = db.relationship('Spell', secondary=student_spells, backref='casters')
	posts = db.relationship('Post', backref='student')

	__mapper_args__ = {
		'polymorphic_identity': 'student'
	}

	def add_points(self, num):
		self.points += num

	def deduct_points(self, num):
		self.points -= num

class Spell(Rankable):
	__tablename__ = 'spells'

	id = db.Column(db.Integer, db.ForeignKey('rankables.id'), primary_key=True)
	cost = db.Column(db.Integer)
	description = db.Column(db.Text)

	__mapper_args__ = {
		'polymorphic_identity': 'spell'
	}

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
	rankable_id = db.Column(db.Integer, db.ForeignKey('rankables.id'))

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