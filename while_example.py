i = 0
while i < 100:
	i += 1
	if i == 7:
		print("Игнорируем семёрку")
		continue
	if i == 20:
		break
	print(1)
else :
	print("Цикл завршён успешно")
print("Цикл не завершён")