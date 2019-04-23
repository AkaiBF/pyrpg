from classes.player import Player, bcolors
from classes.weapon import Weapon

pj1 = Player("Rhogar", 12, 0, 18, 16, 13, 14, 9, 7, 16)
pj2 = Player("Berto", 30, 0, 12, 12, 10, 18, 10, 10, 10)
sword = Weapon(6, "Sword", 1)

while(pj1.hp > 0 and pj2.hp > 0):
	if(pj1.hit(pj2.armor)):
		dmg = sword.attack()
		pj2.hp -= dmg
		print(pj1.name + " ha hecho " + str(dmg) + " de daño")
		if(pj2.hp <= 0):
		 print(pj2.name + " ha muerto")
		 break
	else:
		print(pj1.name + " ha fallado")
	if(pj2.hit(pj1.armor)):
		dmg = sword.attack()
		pj1.hp -= dmg
		print(pj2.name + " ha hecho " + str(dmg) + " de daño")
	else:
		print(pj2.name + " ha fallado")
	if(pj1.hp <= 0):
		print(pj1.name + " ha muerto")