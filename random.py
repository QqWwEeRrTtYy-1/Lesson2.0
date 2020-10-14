import random

while number < guess and number > guess:
guess = int(input("Угадай число от 1-ого до 3-ех, которое загадал компьютер "))
number = random.randinteger(1, 3)
if number == guess:
	print("Ты угадал!")
	break
input("Нажмите ENTER чтобы продолжить ")
