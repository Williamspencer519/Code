class Actor:
	def __init__(self):
		self.hp = 100
		self.defence = 10
		self.form = "human"

	def take_damage(self, damage):
		pass


class Druid(Actor):
	def __init__(self):
		self.attack_power = 2
		super(Druid, self).__init__()
		pass
	def transform(self, new_form):
		pass

	def moonfire(self):
		'''return the damage done by moonfire as specified in the test'''
		pass
	