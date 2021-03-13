import re as r

phone = input("Введите ваш номер телефона с кодом +7: ")
def is_number_true(number_adr: str) -> bool:
	alphabet = r.findall(r"[^+1234567890]", number_adr)
	num = r.findall(r"\d", number_adr)
	code = r.findall(r"^[+]", number_adr)
	if len(alphabet) == 0:
		if code == ["+"]:
			if len(num) == 11 and num[0] == "7":
				return True 
			else:
				return False
		else:
			return False
	else:
		return False

finish = is_number_true(phone)
print(finish)
