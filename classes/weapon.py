import random

class Weapon:
	def __init__(self, dmg, name, hands):
		self.maxDmg = dmg
		self.minDmg = 1
		self.name = name
		self.hands = hands

	def attack(self):
		return random.randrange(self.minDmg, self.maxDmg)