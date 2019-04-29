class Item:
	def __init__(self, quantity, rarity, effect):
		self.quantity = quantity
		self.rarity = rarity
		self.effect = effect

	def heal(self, player):
		self.quantity -= 1
		player.hp += random.randrange(1, 6)

	def use(self, player, enemy):
		if(self.effect == 0):
			self.heal(player)
		if(self.effect == 1):
			player.imposeAdvantage()
