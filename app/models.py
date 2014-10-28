from . import db

class Rankable(db.Model):
	__tablename__ = 'rankables'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))
	type = db.Column(db.String(40))
	rankings = db.Relationship('Ranking', backref='rankable')

	__mapper_args__ = {
		'polymorphic_identity': 'rankable',
		'polymorphic_on': type,
	}

class Student(Rankable):
	__tablename__ = 'students'

	id = db.Column(db.Integer, db.ForeignKey('rankables.id'), primary_key=True)
	points = db.Column(db.Integer, default=0)

	__mapper_args__ = {
		'polymorphic_identity': 'student'
	}

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
	rank = db.Relationship('Rank', backref='rankings')
	tree = db.Relationship('Tree', backref='rankings')

	rankable_id = db.Column(db.Integer, db.ForeignKey('rankables.id'))