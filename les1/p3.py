import turtle
from turtle import *


def turt():

    begin_fill()
    turtle.speed(10)
    for step in range(6):
        for i in range(3):
            turtle.forward(50)
            turtle.left(360/3)
        turtle.forward(50)
        turtle.right(60)
    turtle.hideturtle()
    end_fill()


turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('blue')
turtle.forward(100)

color('blue', 'yellow')
turt()

turtle.backward(200)

color('blue', 'gray')
turt()

done()
