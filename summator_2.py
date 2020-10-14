def summator(*number: int):
	""" Принимает числа и возвращает их сумму в виде целого числа  """
	summa_vseh_objectov = 0
	for i in number:
		summa_vseh_objectov += i
	return summa_vseh_objectov

print(summator(1, 2, 3, 4, 55))