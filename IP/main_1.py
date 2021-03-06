#СПРАШИВАЕМ IP
IP = input("Введите ваш IP для проверки: ")

#ПРОВЕРКА IP
def is_IP_true(IP_adr: str) -> bool:
	if not IP_adr:
		return False

	#НЕ ДОЛЖНО БЫТЬ БУКВ
	for i in IP_adr:
		if i.isalpha():
			return False

	#НЕ БОЛЬШЕ 255 И НЕ МЕНЬШЕ 0
	IP_list = IP_adr.split('.')
	for i in IP_list:
		if int(i) > 255 or int(i) <0:
			return False

	#НЕ БОЛЬШЕ 3 ТОЧЕК
	if IP_adr.count(".") != 3:
		return False

	#НЕ БОЛЬШЕ 15 СИМВОЛОВ
	if len(IP_adr) > 15:
		return False

	#НЕ ДОЛЖНО БЫТЬ ПРОБЕЛОВ
	if IP_adr.count(" ") > 0:
		return False

	return True


finish = is_IP_true(IP)
print(finish)
