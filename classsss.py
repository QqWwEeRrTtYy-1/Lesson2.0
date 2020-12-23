class Orc():
    # атрибуты класса
    name = ""
    mood = ""
    hp = 100
    inventory = []

    # методы класса
    def __init__(self, name, mood, hp, inventory):
        self.name = name
        self.mood = mood
        self.hp = hp
        self.inventory = inventory

    def introduce(self):
        print(self.name)
        print(self.mood)
        print(self.hp)
        print(*self.inventory, sep = ", ")

    def heal(self, add_hp):
        self.hp += add_hp

    def full_heal(self):
        self.hp += 100 - self.hp

first_orc = Orc("Василий", "обычное", 100, ["камень", "цель", "монета"])
second_orc = Orc("Генадий", "скверное", 40, [])

first_orc.introduce()
second_orc.full_heal()
second_orc.introduce()