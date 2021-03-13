import turtle
import random


turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()


def draw_square(x,y,width,color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(color)

    pen.begin_fill()
    for i in range(4):
        pen.forward(width)
        pen.left(90)
    pen.end_fill()

def draw_triangle(x,y,width,color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(color)

    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

def draw_rectangle(x,y,width,height,color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(color)

    pen.begin_fill()
    for i in range(4):
        if i % 2 ==0:
            pen.forward(width)
        else:
            pen.forward(height)
            pen.left(90)
    pen.end_fill()
       


draw_triangle(-60,100,50,"red")
draw_square(50,100,50,"pink")
draw_rectangle(50,100,50,"blue")



turtle.done()