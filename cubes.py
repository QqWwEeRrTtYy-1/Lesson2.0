import random 
def throw_cube(tries: int):
	bank = 0
	while tries > 0:
		bank += random.randint(1, 6)
		tries -= 1
	return bank

print(throw_cube(2))