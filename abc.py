import turtle
turtle.reset()
turtle.shape("classic")

def drow_deshed_line(length:int, color:str):
    """Рисует штриховую линию из центра length и color цвета"""
    for i in range(length):
        turtle.color(color)
        turtle.pendown()
        turtle.fd(10)
        turtle.penup()
        turtle.fd(10)

drow_deshed_line(15, "red")
turtle.mainloop()