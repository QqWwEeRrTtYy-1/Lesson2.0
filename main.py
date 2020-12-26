import my_classes as cl
import os
import time

def main():
	global player
	player = cl.Player("Иван", "Иванов", 80, 5, 36)
	player.print_values()

	def fight():
		def create_enemy():
			global enemy
			enemy = cl.Enemy(1)
			enemy.print_values()

		def battle(player, enemy):
			print("Сражение началось!")

			while player.hp > 0 or enemy.hp > 0:
				enemy.change_stats()

		create_enemy()
		battle(player, enemy)
	fight()
main()
