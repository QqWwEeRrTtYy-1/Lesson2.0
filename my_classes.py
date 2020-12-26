import random
class Humanoid():
	def __init__(self):
		self.name = "Имя"
		self.surname = "Фамилия"
		self.level = 1
		self.hp = 100
		self.XP = 0
		#self.weapon = {"Пистолет" : 1}

	def print_values(self):
		print("Имя:", self.name)
		print("Фамилия:", self.surname)
		print("Здоровье:", self.hp)
		print("Уровень:", self.level)
		print("Опыт:", self.XP)

	def change_stats(self, hp_damage):
		self.hp -= hp_damage


class Player(Humanoid):
	def __init__(self, name, surname, hp, level, XP):
		super().__init__()
		self.name = name
		self.surname = surname
		self.level = level
		self.hp = hp
		self.XP = XP

class Enemy(Humanoid):
	def __init__(self, level):
		super().__init__()
		self.name = random.choice(("Пётр", "Алексей", "Александр"))
		self. surname = random.choice(("Петров", "Алексеев", "Александров"))
		self.level = level
		self.hp = 100
