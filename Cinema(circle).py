money = int(input("Вам нужно купить билет стоимостью 350 рублей, сколько у вас денег? "))
age = int(input("Сколько вам лет? "))
if money < 350:
    print("У вас недостаточно денег. Необходимо добавить", (350 - money))
elif money == 350:
    print("Вы дали полную сумму без сдачи \nВам дали только билет")
else:
    print("Вам дали билет и сдачу в размере ",(money - 350))
input("Нажмите ENTER чтобы продолжить")