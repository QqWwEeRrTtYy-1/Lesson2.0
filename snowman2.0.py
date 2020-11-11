import turtle

def draw_snowman(color:str, collichestvo:int, razmer_niz:int):
	for i in range(collichestvo):
		turtle.circle(-1 * razmer_niz)
		razmer_niz -= 20

draw_snowman("red", 3, 100)
turtle.mainloop()