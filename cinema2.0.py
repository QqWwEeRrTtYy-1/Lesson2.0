people = int(input("Один билет стоит 400 рублей, сколько вам нужно билетов? "))
money = int(input("Сколько у вас денег? "))
if (money * people) == (400 * people):
	print("Вам дали билеты в колличестве ",people,"штук")
elif (money * people) < (400 * people):
	print("У вас недостаточно денег")
else:
	print("Вам дали билеты в колличестве", people ,"штук и сдачу в размере ",(money - (400 * people)))
input("Нажмите ENTER чтобы продолжить")