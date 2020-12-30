import random

class Humanoid():
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.level = 1
        self.hp = 100
        self.attack = 0
        self.weapon = ""

    def print_stats(self):
        print(self.name, self.surname)
        print("Уровень:", self.level)
        print("Здоровье:", self.hp)
        print("Оружие:", self.weapon)
        print("Урон:", self.attack)
        print()

    def change_stats(self, hp_damage):
        self.hp -= hp_damage


class Player(Humanoid):
    def __init__(self, name, surname, level, hp, attack):
        super().__init__()
        self.name = name
        self.surname = surname
        self.level = level
        self.hp = hp
        self.weapon = random.choice(("Меч", "Палица", "Дубина"))
        if self.weapon == "Меч":
            self.attack = 7
        elif self.weapon == "Палица":
            self.attack = 5
        elif self.weapon == "Дубина":
            self.attack = 3


class Enemy(Humanoid):
    def __init__(self, level):
        super().__init__()
        self.name = random.choice(("Грэг", "Аргк", "Хемс"))
        self.surname = random.choice(("Дерзкий", "Алчный", "Зловонный"))
        self.level = level
        self.hp = 100
        self.weapon = random.choice(("Булава", "Двуручный меч", "Палка"))
        if self.weapon == "Булава":
            self.attack = 5
        elif self.weapon == "Двуручный меч":
            self.attack = 6
        elif self.weapon == "Палка":
            self.attack = 2