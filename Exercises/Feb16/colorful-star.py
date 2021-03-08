import turtle
import random
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(5)
pen.hideturtle()


colors = ("yellow", "green", "orange","cornsilk", "teal","red", "black" )

for i in range (100):
    starWidth = random.randint(20,80)
    x = random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2))
    y = random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/2))
    color = random.choice(colors)
    pen.color(color)
    #set the position 
    #the draw a line of star width
    pen.up()
    pen.setpos(x,y)
    pen.down()

    #draw top triangle 
    pen.begin_fill()
    for j in range(3):
        pen.forward(starWidth)
        pen.left(120)
    pen.end_fill()

    #draw bottom circle
    pen.up()
    pen.setpos(x, y + starWidth/2)
    pen.down()
    pen.begin_fill()
    for j in range(3):
        pen.forward(starWidth)
        pen.left(-120)
    pen.end_fill()

turtle.done()