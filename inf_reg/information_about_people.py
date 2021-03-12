import re as r
#СПРАШИВАЕМ ДАННЫЕ ПОЛЬЗОВАТЕЛЯ
surname = input("Введите вашу фамилию: ")
"""name = input("Введите ваше имя: ")
patronymic = input("Введите ваше отчество: ")
birthday = input("Введите вашу дату рождения в формате 9.09.2009: ")

count = 0"""

#ФУНКЦИЯ ПРОВРКИ
def is_surname_true(Sur_d: str) -> str:
	alphabet = r.findall(r"[\D\w]", Sur_d)
	if len(alphabet) > 0:
		print(1)
	else:
		print(2)


surname_finish = is_surname_true(surname)

#ФУНКЦИЯ ПРОВРКИ
"""def is_name_true(Name_d: str) -> str:
	alphabet = r.findall(r"[^.1234567890]", Name_d)

name_finish = is_name_true()

#ФУНКЦИЯ ПРОВРКИ
def is_patronymic_true(Patr_d: str) -> str:
	alphabet = r.findall(r"[^.1234567890]", Patr_d)

patronymic_finish = is_patronymic_true()

#ФУНКЦИЯ ПРОВРКИ
def is_birthday_true(IP_adr: str) -> str:
	alphabet = r.findall(r"[^.1234567890]", IP_adr)
	points = r.findall(r"[.]", IP_adr)
	numbers = r.findall(r"[.1234567890]", IP_adr)
	numbers_split = r.split(r"[.]", IP_adr)

	#ФУНКЦИЯ СРАВНЕНИЯ С 0, 256 И ПУСТОЙ СТРОКОЙ
	def zeroes(number_of_split):
		if number_of_split != "" and int(number_of_split) < 256 and str(number_of_split) != "000" and str(number_of_split) != "00":
			number = list(number_of_split)
			count = 1
		else:
			count = 2
		return count

birthday_finish = is_birthday_true()"""
