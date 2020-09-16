import random

input("Нажмите ENTER чтобы сыграть в русскую рулетку ")
user_score = random.randrange(1, 6)
if user_score == 1:
	print("Вы выжили!")
else :
	print("Вы выстрелили!")
input("Нажмите ENTER чтобы продолжить ")