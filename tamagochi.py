from os import system

tamagoch = {
    "Кличка:": "Федя",
    "Счастье:": 80,
    "Голод:": 75,
    "Здоровье:": 100,
}

global user_choise
user_choise = 0

def show_pet(tamagoch):
	for key, value in tamagoch.items():
		print(key, value)

show_pet(tamagoch)

while user_choise not in (1, 2, 3):
    user_choise = int(input("\nИнструкция: \n1 - покормить \n2 - поиграть \n3 - ничего не делать \n"))
    system('cls')
    if user_choise == 1:
    	def feed(tamagoch):
            print("Вы решили покормить Федю. Сытость поднялась на 15\n")
            tamagoch["Голод:"] += 15
            
        feed(tamagoch)

    elif user_choise == 2:
        print("Вы решили поиграть с Федей. Счастье поднялось на 20\n")
        tamagoch["Счастье:"] += 20
    else :
        print("Вы решили ничего не делать. Счастье и здоровье понизились на 5\n")
        tamagoch["Счастье:"] -= 5
        tamagoch["Здоровье:"] -= 5

def show_pet(tamagoch):
	for key, value in tamagoch.items():
		print(key, value)

show_pet(tamagoch)
