"""
def test():
    print("ABCDEFG")
    return None

test()
"""

"""функция
принимает чемоданы
смотрит их содержимое
сравнивает содержимое со списком
возвращает True если нет запрета
возвращает False если запрет обнаружен """

suitcase1 = ["Пиджак", "Граната"]
suitcase2 = ["Футболка", "Кроссовки"]
forbidden = ["Граната", "Ножницы"]

all_suitcases = (suitcase1, suitcase2)

def suitcase_is_safe(scan: list):
    """ Принимает список, возвращает True или False """
    for scan in all_suitcases:
	    for thing in scan:
	        if thing in forbidden:
	            return False 
	        else:
	        	continue
	    return True

print(suitcase_is_safe(all_suitcases)) 
