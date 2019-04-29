from classes.player import Player, bcolors
from classes.weapon import Weapon
from classes.spell import Spell
from classes.item import Item

pj1 = Player("Rhogar", 12, 45, 18, 16, 13, 14, 9, 7, 16)
pj2 = Player("Berto", 30, 30, 12, 12, 10, 18, 10, 10, 10)
sword = Weapon(6, "Sword", 1)
healingSpell = Spell(12, 7, 5)
fireball = Spell(6, 1, 12)
advantager = Item(1, 'common', 1)
advantager.use(pj1, pj2)

def menu():
	print("Acciones")
	print("1. Usar espada")
	print("2. Curar")
	print("3. Usar bola de fuego")
	print("Elije una acción:", end="")
	return input()

while(pj1.hp > 0 and pj2.hp > 0):
	'''Turno jugador'''
	action = menu()
	print(action)
	if(int(action) == 1):
		if(pj1.hit(pj2.armor)):
			dmg = sword.attack()
			pj2.hp -= dmg
			print(pj1.name + " ha hecho " + str(dmg) + " de daño")
			if(pj2.hp <= 0):
			 print(pj2.name + " ha muerto")
			 break
		else:
			print(pj1.name + " ha fallado")
	elif(int(action) == 2):
		if(pj1.mp > healingSpell.cost):
			pj1.hp -= healingSpell.attack()
		else:
			print("No tienes suficiente maná")
			continue
	elif(int(action) == 3):
		if(pj1.mp > fireball.cost):
			pj2.hp -= fireball.attack()
		else:
			print("No tienes suficiente maná")
			continue
	else:
		print("Acción inválida")
		continue
	''' Turno NPC '''
	if(pj2.hit(pj1.armor)):
		dmg = sword.attack()
		pj1.hp -= dmg
		print(pj2.name + " ha hecho " + str(dmg) + " de daño")
	else:
		print(pj2.name + " ha fallado")
	if(pj1.hp <= 0):
		print(pj1.name + " ha muerto")
	print(pj1.name + "'s HP:" + str(pj1.hp))
	print(pj2.name + "'s HP:" + str(pj2.hp))