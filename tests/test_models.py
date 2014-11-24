import unittest
from datetime import datetime
from app import create_app, db
from app.models import *

class ModelsTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_default_student_points(self):
		stud = Student()
		db.session.add(stud)
		db.session.commit()
		self.assertEqual(stud.points, 0)

	def test_students_have_multiple_rankings(self):
		stud = Student(name="me")
		rank1 = Rank(name="rank1")
		tree1 = Tree(name="tree1")
		ranking1 = Ranking(student=stud, rank=rank1, tree=tree1)

		db.session.add(ranking1)
		db.session.commit()

		self.assertEqual(stud.rankings[0], ranking1)

		rank2 = Rank(name="rank2")
		tree2 = Tree(name="tree2")
		ranking2 = Ranking(student=stud, rank=rank2, tree=tree2)

		db.session.add(ranking2)
		db.session.commit()

		self.assertEqual(stud.rankings[1], ranking2)

	def test_ranking_title(self):
		rank = Rank(name="Rank!")
		tree = Tree(name="Tree!")
		ranking = Ranking(rank=rank, tree=tree)
		self.assertEqual("Rank! - Tree!", ranking.title())

	def test_students_gaining_and_losing_points(self):
		stud = Student(name="Me")
		db.session.add(stud)
		db.session.commit()

		stud.add_points(50)

		self.assertEqual(stud.points, 50)

		stud.deduct_points(50)

		self.assertEqual(stud.points, 0)

	def test_students_have_many_spells(self):
		stud = Student(name="Me")
		spell1 = Spell(name="Firaga")
		spell2 = Spell(name="Thundaga")
		spell1.caster = stud
		spell2.caster = stud
		db.session.add(stud)
		db.session.commit()

		self.assertIn(spell1, stud.spells)
		self.assertIn(spell2, stud.spells)

	def test_spells_have_caster(self):
		spell = Spell(name="Thundaga")
		stud = Student(name="Lightning")
		stud.spells.append(spell)
		db.session.add(spell)
		db.session.commit()

		self.assertEqual(stud, spell.caster)

	def test_spell_description(self):
		spell = Spell(name="Thundaga", description="Big ass lightnin bolt")

		self.assertEqual(spell.description, "Big ass lightnin bolt")

	def test_spell_approval_purchase(self):
		spell = Spell(name="Thundaga")
		db.session.add(spell)
		db.session.commit()

		self.assertFalse(spell.approved)
		self.assertFalse(spell.purchased)

	def test_post_created_at(self):
		now = datetime.now()
		post = Post(created_at=now)
		db.session.add(post)
		db.session.commit()

		self.assertEqual(now, post.created_at)

	def test_student_has_many_posts(self):
		stud = Student(name="Someone")
		post1 = Post(body="post 1")
		post2 = Post(body="post 2")
		stud.posts.append(post1)
		stud.posts.append(post2)
		db.session.add(stud)
		db.session.commit()

		self.assertIn(post1, stud.posts)
		self.assertIn(post2, stud.posts)

	def test_many_posts_to_many_tags(self):
		post = Post(body="Post 1")
		tag = Tag(name="Tag 1")

		post.tags.append(tag)
		db.session.add(post)
		db.session.commit()

		self.assertIn(tag, post.tags)
		self.assertIn(post, tag.posts)

	def test_students_are_not_admins_by_default(self):
		stud = Student(name="Nigger")
		db.session.add(stud)
		db.session.commit()

		self.assertFalse(stud.admin)

	# room tests
	def test_room_has_posts(self):
		room = Room(name="Bathroom", description="Go on the pot")
		user = Student(name="poster")
		post = Post(body="The first post in the world!")
		user.posts.append(post)
		room.posts.append(post)

		db.session.add(room)
		db.session.commit()

		self.assertIn(post, room.posts)

	def test_post_has_room(self):
		room = Room(name="Bathroom", description="Go on the pot")
		user = Student(name="poster")
		post = Post(body="The first post in the world!")
		user.posts.append(post)
		room.posts.append(post)

		db.session.add(room)		
		db.session.commit()

		self.assertEqual(room, post.room)

	def test_closed_posts(self):
		post = Post(body="TESTING")
		db.session.add(post)
		db.session.commit()

		self.assertFalse(post.closed)