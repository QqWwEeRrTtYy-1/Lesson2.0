x = 1

print(x, "был снаружи")

def fun_x():
	global x
	x += 2
	print(x, "внутри")

fun_x()

x -= 1

print(x, "стал снаружи")