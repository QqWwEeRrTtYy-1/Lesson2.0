import random

input("Нажмите ENTER чтобы бросить кости ")
user_score = random.randrange(2, 12)
computer_score = random.randrange(2, 12)
print("У вас ", user_score , " У соперника " , computer_score)
if user_score == computer_score:
	print("Ничья!")
elif user_score > computer_score:
	print("Вы выиграли!")
else :
	print("Вы проиграли!")
input("Нажмите ENTER чтобы продолжить ")