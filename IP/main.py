def cat_jumps(minutes: int) -> int:
	"""
		doc
	"""
	amount = minutes // 10
	amount_jumps = amount * 3
	return amount_jumps

finish = cat_jumps(40)
print(finish)
print(type(12))

assert cat_jumps(10) == 3, "Неверное значение"
assert cat_jumps(15) == 3, "Неверное значение"
assert cat_jumps(40) == 12, "Неверное значение"