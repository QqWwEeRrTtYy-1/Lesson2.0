import re as r
#СПРАШИВАЕМ IP-адрес
IP = input("Введите ваш IP-адрес для проверки: ")

#ФУНКЦИЯ ПРОВРКИ
def is_IP_true(IP_adr: str) -> bool:
	alphabet = r.findall(r"[^.1234567890]", IP_adr)
	points = r.findall(r"[.]", IP_adr)
	numbers = r.findall(r"[.1234567890]", IP_adr)
	numbers_split = r.split(r"[.]", IP_adr)

	count = 0

	#ФУНКЦИЯ СРАВНЕНИЯ С 0, 256 И ПУСТОЙ СТРОКОЙ
	def zeroes(number_of_split):
		if number_of_split != "" and int(number_of_split) < 256 and str(number_of_split) != "000" and str(number_of_split) != "00":
			number = list(number_of_split)
			count = 1
		else:
			count = 2
		return count

	#СРАВНЕНИЕ
	if len(alphabet) == 0:
		if len(points) == 3:
			if zeroes(numbers_split[0]) == 1:
				if zeroes(numbers_split[1]) == 1:
					if zeroes(numbers_split[2]) == 1:
						if zeroes(numbers_split[3]) == 1:
							return True
						else:
							return False
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False

finish = is_IP_true(IP)
print(finish)