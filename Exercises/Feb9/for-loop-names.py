# Author: Talha Gill

import turtle
import random

turtle.bgcolor("pink")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0)
pen.color("black")
style = ("Arial", 12, "normal")
pen.hideturtle()
turtle.colormode(255)


numNames = int(turtle.numinput("Names", "Num Names: ", 10,1,100))

#Loop and Draw the user name
for i in range(numNames):
    x = random.randint(int(-turtle.window_width()/2),int(turtle.window_width()/2))
    y = random.randint(int(-turtle.window_height()/2),int(turtle.window_height()/2))
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue =  random.randint(0,255)
    pen.color(red,green,blue)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.write("Talha", font = style)
























turtle.done()