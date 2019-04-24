import random

class Spell:
	def __init__(self, dmg, dmgType, cost):
		self.dmg = dmg
		self.dmgType = dmgType
		self.cost = cost

	def getDamageTypeName(self):
		typeNames = {
			0: "None",
			1: "Fire",
			2: "Ice",
			3: "Electric",
			4: "Radiant",
			5: "Necrotic",
			6: "Force",
			7: "Healing"
		}
		return typeNames.get(self.dmgType)

	def attack(self):
		if(self.dmgType == 7):
			return -(random.randrange(1, self.dmg))
		if(self.dmgType != 0):
			return random.randrange(1, self.dmg)