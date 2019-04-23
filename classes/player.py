import random

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class Player:
	def __init__(self, name, maxHp, maxMp, armor, strength, 
							 dextery, constitution, intelligence, wisdom, charisma):
		self.name = name
		self.maxHp = maxHp
		self.hp = maxHp
		self.maxMp = maxMp
		self.mp = maxMp
		self.armor = armor
		self.strength = strength
		self.dextery = dextery
		self.constitution = constitution
		self.intelligence = intelligence
		self.wisdom = wisdom
		self.charisma = charisma

	def hit(self, armor):
		return (random.randrange(1, 20) + self.getMod(self.strength)) >= armor

	def getMod(self, stat):
		return (stat - 10)/2

	def disadvantageHit(self, armor):
		if(self.hit(armor) and self.hit(armor)):
			return True
		else:
			return False

	def advantageHit(self, armor):
		if(self.hit(armor) or self.hit(armor)):
			return True
		else:
			return False


