"""печатаем числа от 1 до 100
если чсило делится на 3, печатаем Fizz
если чсило делится на 5, печатаем Buzz
если чсило делится и на 3, и на 5 печатаем FizzBuzz
остальные печатаем без изменений"""

def fizzbuzz():
	for i in range(1, 100):
		if i % 3 == 0 and i % 5 == 0:
				print("FizzBuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)

fizzbuzz()