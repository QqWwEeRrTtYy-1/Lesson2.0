print("Вас привели в комнату. ")
print("Перед вами 3 коробки с номерами: 1, 2 или 3.")

answer = 0
while answer not in ("1", "2", "3"):
    print("""
    1 коробка - из дерева, маленького размера
    2 коробка - из металла, большого размера
    3 коробка - из картона, среднего размера
    """)
    answer = input("Какую решаете открыть? ")
    if answer == "2":
        print("В коробке была ядовитая змея \nОна укусила вас, после чего вы скончались от яда.")
    elif answer == "3":
        print("В коробке был улей лесных пчёл, вас покусали.")
    elif answer == "1":
        print("Вы взяли книгу, после чего открыли её \nТам была инструкция, как выбраться из комнаты. \nВы выбрались на свободу")
    else :
        print("")
else :
    print("Конец")
