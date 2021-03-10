import re as r

#IP = input("Введите ваш IP для проверки: ")
def is_IP_true(IP_adr: str) -> bool:
	alph = r.findall(r"[^.1234567890]", IP_adr)
	points = r.findall(r"[.]", IP_adr)
	numbers = r.findall(r"[.1234567890]", IP_adr)
	numbers_split = r.split(r"[.]", IP_adr)
	if len(alph) == 0:
		if len(points) == 3:
			if numbers_split[0] != "" and int(numbers_split[0]) < 256 and str(numbers_split[0]) != "000" and str(numbers_split[0]) != "00":
				if numbers_split[1] != "" and int(numbers_split[1]) < 256 and str(numbers_split[1]) != "000" and str(numbers_split[1]) != "00":
					if numbers_split[2] != "" and int(numbers_split[2]) < 256 and str(numbers_split[2]) != "000" and str(numbers_split[2]) != "00":
						if numbers_split[3] != "" and int(numbers_split[3]) < 256 and str(numbers_split[3]) != "000" and str(numbers_split[3]) != "00":
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

finish = is_IP_true("0.1.0.251")
print(finish)
