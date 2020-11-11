import turtle
turtle.reset()
turtle.shape("turtle")
turtle.pencolor("#D3D3D3")
turtle.color("#D3D3D3")
turtle.pensize(1)

turtle.begin_fill()
turtle.circle(30)
turtle.lt(180)
turtle.circle(40)
turtle.circle(40, 180)
turtle.lt(180)
turtle.circle(50)
turtle.end_fill()

turtle.mainloop()