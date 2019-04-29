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
		self.advantage = 0

	def hit(self, armor):
		if(self.advantage < 0):
			return self.disadvantageHit(armor)
		if(self.advantage > 0):
			return self.advantageHit(armor)
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

	def dexST(self, dc):
		return (random.randrange(1, 20) + self.getMod(self.dextery)) >= dc

	def consST(self, dc):
		return (random.randrange(1, 20) + self.getMod(self.constitution)) >= dc

	def intST(self, dc):
		return (random.randrange(1, 20) + self.getMod(self.intelligence)) >= dc

	def wisST(self, dc):
		return (random.randrange(1, 20) + self.getMod(self.wisdom)) >= dc

	def charST(self, dc):
		return (random.randrange(1, 20) + self.getMod(self.charisma)) >= dc

	''' ADVANTAGE/DISADVANTAGE CONTROL '''
	def imposeAdvantage(self):
		self.advantage += 1

	def imposeDisadvantage(self):
		self.advantage -= 1

	def normalizeAdvantage(self):
		if(self.advantage > 0):
			self.advantage -= 1
		if(self.advantage < 0):
			self.advantage += 1

	def resetAdvantage(self):
		self.advantage = 0