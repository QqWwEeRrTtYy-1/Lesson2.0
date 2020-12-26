import random
import time
import os

#Суперкласс
class Values:
    def __init__(self, name = "Unknown"):
        self.health = 100
        self.name = name
        self.speed = 5


    def show_info(self):
        print(self.health, self.name, sep = "\n")

    def fight(self):
        self.health -= random.randint(5, 12)

    def middle_fight(self):
        self.health -= random.randint(1,5)

    def turbo_fight(self):
        self.health -= random.randint(15, 25)

    def healing(self):
        self.health += random.randint(20, 50)

    def middle(self):
        self.health -= 20
        self.speed += 10

    def berserk(self):
        self.health += 20
        self.speed += 5

    def player_values(self):
        self.speed += 5


#Подкласс
class Zombie(Values):
    pass


#Подкласс
class Player(Values):
    pass


zombie_names = ["Мутировавший зомби", "Ужасающий зомби", "Разъярённый зомби"]
player_names = ["Мудрец", "Разрушитель", "Каратель"]

zombie_fight_1 = Zombie(random.choice(zombie_names))
zombie_fight_2 = Zombie(random.choice(zombie_names))
zombie_fight_3 = Zombie(random.choice(zombie_names))
player_fight = Player(random.choice(player_names))

def mortal_kombat():
    def round_one():
        global result
        result = 0

        print("ПЕРВЫЙ РАУНД!")

        zombie_class = random.randint(1,3)
        if zombie_class == 1:
            print("Класс: зомби - обычный")
        if zombie_class == 2:
            print("Класс: зомби - бегун")
            zombie_fight_1.middle()
        if zombie_class == 3:
            print("Класс: зомби - Берсерк")
            zombie_fight_1.berserk()

        zombie_fight_1.health -= 60

        if player_fight.health < 50:
            player_fight.speed = 5
        elif player_fight.health >= 50:
            player_fight.speed = 10

        print(player_fight.name, "-", player_fight.health, "HP,", zombie_fight_1.name, "-", zombie_fight_1.health, "HP")
        
        time.sleep(2)
        os.system("cls")

        print("БОЙ НАЧАЛСЯ!")
        
        while player_fight.health > 0 and zombie_fight_1.health > 0:
            player_kombat = random.randint(1, 4)
            zombie_dodge = random.randint(5, 15)
            if player_kombat == 1:
                if zombie_fight_1.speed == zombie_dodge:
                    print(zombie_fight_1.name, "увернулся")
                else:
                    print(player_fight.name, "стреляет из пистолета")
                    zombie_fight_1.turbo_fight()
            elif player_kombat == 2:
                if zombie_fight_1.speed == zombie_dodge:
                    print(zombie_fight_1.name, "увернулся")
                else:
                    print(player_fight.name, "бьёт руками")
                    zombie_fight_1.fight()
            elif player_kombat == 3:
                if zombie_fight_1.speed == zombie_dodge:
                    print(zombie_fight_1.name, "увернулся")
                else:
                    print(player_fight.name, "толкнул в сторону")
                    zombie_fight_1.middle_fight()
            elif player_kombat == 4:
                print(player_fight.name, "нашёл аптечку")
                player_fight.healing()

            time.sleep(0.5)

            zombie_kombat = random.randint(1, 7)
            player_dodge = random.randint(5, 15)
            if zombie_kombat == 1 or 5:
                if player_fight.speed == player_dodge:
                    print(player_fight.name, "увернулся")
                else:
                    print(zombie_fight_1.name, "вгрызается в шею")
                    player_fight.turbo_fight()
            elif zombie_kombat == 2 or 6:
                if player_fight.speed == player_dodge:
                    print(player_fight.name, "увернулся")
                else:
                    print(zombie_fight_1.name, "вгрызается в руки")
                    player_fight.fight()
            elif zombie_kombat == 3 or 7:
                if player_fight.speed == player_dodge:
                    print(player_fight.name, "увернулся")
                else:
                    print(zombie_fight_1.name, "навалился")
                    player_fight.middle_fight()
            elif zombie_kombat == 4:
                print(zombie_fight_1.name, "съел останки трупа")
                zombie_fight_1.healing()

            time.sleep(0.5)

            if player_fight.health < 0:
                player_fight.health = 0
            elif player_fight.health > 100:
                player_fight.health = 100

            if zombie_fight_1.health < 0:
                zombie_fight_1.health = 0
            elif zombie_fight_1.health > 100 and zombie_class == 1:
                zombie_fight_1.health = 100
            elif zombie_fight_1.health > 120 and zombie_class == 2:
                zombie_fight_1.health = 120
            elif zombie_fight_1.health > 150 and zombie_class == 3:
                zombie_fight_1.health = 150

            print(player_fight.name, "-", player_fight.health, "HP,", zombie_fight_1.name, "-", zombie_fight_1.health, "HP")

            if player_fight.health <= 0:
                print(zombie_fight_1.name, "выиграл!")
                print("Попробуй ещё раз!")
                result = 1
                break
            elif zombie_fight_1.health <= 0:
                print(player_fight.name, "выиграл!")
                result = 2
            elif zombie_fight_1.health <= 0 and player_fight.health <= 0:
                print("Все умерли!")
                break

            time.sleep(2)
            os.system("cls")

            if result == 2:
                def round_two():
                    global result
                    result = 0

                    print("ВТОРОЙ РАУНД!")

                    zombie_class = random.randint(1,3)
                    if zombie_class == 1:
                        print("Класс: зомби - обычный")
                    if zombie_class == 2:
                        print("Класс: зомби - бегун")
                        zombie_fight_2.middle()
                    if zombie_class == 3:
                        print("Класс: зомби - Берсерк")
                        zombie_fight_2.berserk()

                    player_fight.health = 100
                    zombie_fight_2.health -= 40

                    if player_fight.health < 50:
                        player_fight.speed = 5
                    elif player_fight.health >= 50:
                        player_fight.speed = 10

                    print(player_fight.name, "-", player_fight.health, "HP,", zombie_fight_2.name, "-", zombie_fight_2.health, "HP")
                    
                    time.sleep(2)
                    os.system("cls")

                    print("БОЙ НАЧАЛСЯ!")
                    
                    while player_fight.health > 0 and zombie_fight_2.health > 0:
                        player_kombat = random.randint(1, 4)
                        zombie_dodge = random.randint(5, 15)
                        if player_kombat == 1:
                            if zombie_fight_2.speed == zombie_dodge:
                                print(zombie_fight_2.name, "увернулся")
                            else:
                                print(player_fight.name, "стреляет из пистолета")
                                zombie_fight_2.turbo_fight()
                        elif player_kombat == 2:
                            if zombie_fight_2.speed == zombie_dodge:
                                print(zombie_fight_2.name, "увернулся")
                            else:
                                print(player_fight.name, "бьёт руками")
                                zombie_fight_2.fight()
                        elif player_kombat == 3:
                            if zombie_fight_2.speed == zombie_dodge:
                                print(zombie_fight_2.name, "увернулся")
                            else:
                                print(player_fight.name, "толкнул в сторону")
                                zombie_fight_2.middle_fight()
                        elif player_kombat == 4:
                            print(player_fight.name, "нашёл аптечку")
                            player_fight.healing()

                        time.sleep(0.5)

                        zombie_kombat = random.randint(1, 7)
                        player_dodge = random.randint(5, 15)
                        if zombie_kombat == 1 or 5:
                            if player_fight.speed == player_dodge:
                                print(player_fight.name, "увернулся")
                            else:
                                print(zombie_fight_2.name, "вгрызается в шею")
                                player_fight.turbo_fight()
                        elif zombie_kombat == 2 or 6:
                            if player_fight.speed == player_dodge:
                                print(player_fight.name, "увернулся")
                            else:
                                print(zombie_fight_2.name, "вгрызается в руки")
                                player_fight.fight()
                        elif zombie_kombat == 3 or 7:
                            if player_fight.speed == player_dodge:
                                print(player_fight.name, "увернулся")
                            else:
                                print(zombie_fight_2.name, "навалился")
                                player_fight.middle_fight()
                        elif zombie_kombat == 4:
                            print(zombie_fight_2.name, "съел останки трупа")
                            zombie_fight_2.healing()

                        time.sleep(0.5)

                        if player_fight.health < 0:
                            player_fight.health = 0
                        elif player_fight.health > 100:
                            player_fight.health = 100

                        if zombie_fight_2.health < 0:
                            zombie_fight_2.health = 0
                        elif zombie_fight_2.health > 100 and zombie_class == 1:
                            zombie_fight_2.health = 100
                        elif zombie_fight_2.health > 120 and zombie_class == 2:
                            zombie_fight_2.health = 120
                        elif zombie_fight_2.health > 150 and zombie_class == 3:
                            zombie_fight_2.health = 150

                        print(player_fight.name, "-", player_fight.health, "HP,", zombie_fight_2.name, "-", zombie_fight_2.health, "HP")

                        if player_fight.health <= 0:
                            print(zombie_fight_2.name, "выиграл!")
                            print("Попробуй ещё раз!")
                            result = 1
                            break
                        elif zombie_fight_2.health <= 0:
                            print(player_fight.name, "выиграл!")
                            result = 2
                        elif zombie_fight_2.health <= 0 and player_fight.health <= 0:
                            print("Все умерли!")
                            break

                        time.sleep(2)
                        os.system("cls")

                        if result == 2:
                            def round_three():
                                global result
                                result = 0

                                print("ТРЕТИЙ РАУНД!")

                                zombie_class = random.randint(1,3)
                                if zombie_class == 1:
                                    print("Класс: зомби - обычный")
                                if zombie_class == 2:
                                    print("Класс: зомби - бегун")
                                    zombie_fight_3.middle()
                                if zombie_class == 3:
                                    print("Класс: зомби - Берсерк")
                                    zombie_fight_3.berserk()

                                player_fight.health = 100
                                zombie_fight_3.health -= 25

                                if player_fight.health < 50:
                                    player_fight.speed = 5
                                elif player_fight.health >= 50:
                                    player_fight.speed = 10

                                print(player_fight.name, "-", player_fight.health, "HP,", zombie_fight_3.name, "-", zombie_fight_3.health, "HP")
                                
                                time.sleep(2)
                                os.system("cls")

                                print("БОЙ НАЧАЛСЯ!")
                                
                                while player_fight.health > 0 and zombie_fight_3.health > 0:
                                    player_kombat = random.randint(1, 4)
                                    zombie_dodge = random.randint(5, 15)
                                    if player_kombat == 1:
                                        if zombie_fight_3.speed == zombie_dodge:
                                            print(zombie_fight_3.name, "увернулся")
                                        else:
                                            print(player_fight.name, "стреляет из пистолета")
                                            zombie_fight_3.turbo_fight()
                                    elif player_kombat == 2:
                                        if zombie_fight_3.speed == zombie_dodge:
                                            print(zombie_fight_3.name, "увернулся")
                                        else:
                                            print(player_fight.name, "бьёт руками")
                                            zombie_fight_3.fight()
                                    elif player_kombat == 3:
                                        if zombie_fight_3.speed == zombie_dodge:
                                            print(zombie_fight_3.name, "увернулся")
                                        else:
                                            print(player_fight.name, "толкнул в сторону")
                                            zombie_fight_3.middle_fight()
                                    elif player_kombat == 4:
                                        print(player_fight.name, "нашёл аптечку")
                                        player_fight.healing()

                                    time.sleep(0.5)

                                    zombie_kombat = random.randint(1, 7)
                                    player_dodge = random.randint(5, 15)
                                    if zombie_kombat == 1 or 5:
                                        if player_fight.speed == player_dodge:
                                            print(player_fight.name, "увернулся")
                                        else:
                                            print(zombie_fight_3.name, "вгрызается в шею")
                                            player_fight.turbo_fight()
                                    elif zombie_kombat == 2 or 6:
                                        if player_fight.speed == player_dodge:
                                            print(player_fight.name, "увернулся")
                                        else:
                                            print(zombie_fight_3.name, "вгрызается в руки")
                                            player_fight.fight()
                                    elif zombie_kombat == 3 or 7:
                                        if player_fight.speed == player_dodge:
                                            print(player_fight.name, "увернулся")
                                        else:
                                            print(zombie_fight_3.name, "навалился")
                                            player_fight.middle_fight()
                                    elif zombie_kombat == 4:
                                        print(zombie_fight_3.name, "съел останки трупа")
                                        zombie_fight_3.healing()

                                    time.sleep(0.5)

                                    if player_fight.health < 0:
                                        player_fight.health = 0
                                    elif player_fight.health > 100:
                                        player_fight.health = 100

                                    if zombie_fight_3.health < 0:
                                        zombie_fight_3.health = 0
                                    elif zombie_fight_3.health > 100 and zombie_class == 1:
                                        zombie_fight_3.health = 100
                                    elif zombie_fight_3.health > 120 and zombie_class == 2:
                                        zombie_fight_3.health = 120
                                    elif zombie_fight_3.health > 150 and zombie_class == 3:
                                        zombie_fight_3.health = 150

                                    print(player_fight.name, "-", player_fight.health, "HP,", zombie_fight_3.name, "-", zombie_fight_3.health, "HP")

                                    if player_fight.health <= 0:
                                        print(zombie_fight_3.name, "выиграл!")
                                        print("Попробуй ещё раз!")
                                        result = 1
                                        break
                                    elif zombie_fight_3.health <= 0:
                                        print(player_fight.name, "выиграл!")
                                        print(player_fight.name, "прошёл все раунды и одержал победу!")
                                        result = 2
                                        break
                                    elif zombie_fight_3.health <= 0 and player_fight.health <= 0:
                                        print("Все умерли!")
                                        break

                                    time.sleep(2)
                                    os.system("cls")

                            round_three()

                round_two()

    round_one()

mortal_kombat()
