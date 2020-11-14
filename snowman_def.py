import turtle
turtle.shape("turtle")
turtle.speed("fastest")
turtle.penup()
turtle.goto(0, - 270)
turtle.pendown()


def draw(collichestvo: int, razmer: int, first_color: int):
    for i in range(collichestvo):
        turtle.colormode(255)
        turtle.color(0, 0, first_color)
        turtle.begin_fill()
        turtle.circle(razmer)
        turtle.penup()
        turtle.lt(90)
        turtle.fd(razmer*2)
        turtle.rt(90)
        turtle.pendown()
        turtle.end_fill()
        razmer = razmer * 0.75
        first_color += 40
    turtle.begin_fill()
    turtle.fd(razmer)
    turtle.lt(110)
    turtle.fd(razmer * 1.5)
    turtle.lt(70)
    turtle.fd(razmer)
    turtle.lt(70)
    turtle.fd(razmer * 1.5)
    turtle.lt(110)
    turtle.fd(razmer)
    turtle.end_fill


draw(3, 100, 90)
turtle.mainloop()
