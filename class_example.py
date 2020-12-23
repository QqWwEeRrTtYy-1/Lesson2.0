import random

#Суперкласс
class Values:
    def __init__(self, name = "Unknown"):
        self.health = 100
        self.name = name

    def show_info(self):
        print(self.health, self.name, sep = "\n")

    def fight(self):
        self.health -= random.randint(5, 12)


#Подкласс
class Zombie(Values):
    """def shoot_zombie(self, times):
        #times - колличество раз(колличество ударов)
        for shoot in range(times):
            self.health -= 15"""

    """def hit_zombie(self):
        self.health -= 10"""


#Подкласс
class Player(Values):
    def heal_player(self):
        self.health += 100 - self.health

    """def hit_player(self):
        self.health -= 20"""


"""enemy = Zombie("Zombie_1")
enemy_1 = Zombie("Zombie_2")
enemy_2 = Zombie()

enemy_1.hit_zombie()
enemy_2.shoot_zombie(2)

enemy.show_info()
enemy_1.show_info()
enemy_2.show_info()

friend = Player("Player_123")

friend.hit_player()
friend.heal_player()

friend.show_info()"""

zombie_fight = Zombie("Zombie_fight")
player_fight = Player("Player_fight")

def mortal_kombat():
    while player_fight.health >= 0 or zombie_fight.health >= 0:
        player_fight.fight()

        zombie_fight.fight()

        if player_fight.health <= 0:
            print("Zombie win!")

        if zombie_fight.health <= 0:
            print("Player win!")

mortal_kombat()