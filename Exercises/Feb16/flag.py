import turtle
import random
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(5)
pen.hideturtle()

#draw  blue
pen.up()
pen.setpos(-turtle.window_width()/2, -turtle.window_height()/2)
pen.down()

#draw a blue rectangle
pen.color("blue")
pen.begin_fill()
for i in range(4):
    if i % 2 ==0: #if i even, divided by 2 has no reminder
        pen.forward(turtle.window_width()/2)
    else:
        pen.forward(turtle.window_height())
    pen.left(90)
pen.end_fill()

pen.color("red")
stripeHeight = turtle.window_height()/13
stripeWidth = turtle.window_height()/2

for i in range(0,13,2):
    pen.up()
    y = -turtle.window_height()/2 + stripeHeight * i
    pen.setpos(0,y)
    pen.down()

    # draw red band
    pen.begin_fill()
    for j in range(4):
        if j % 2 == 0: #if even
            pen.forward(stripeWidth)
        else:
            pen.forward(stripeHeight)
        pen.left(90)
    pen.end_fill()

starWidth = 20
#draw stars
for i in range(50):
    x = random.randint(-int(turtle.window_width()/2),-starWidth)
    y = random.randint(-int(turtle.window_height()/2) + starWidth, int(turtle.window_height()/2)-starWidth)

    pen.up()
    pen.setpos(x,y)
    pen.down()

    pen.color("white")
    # draw a star
    pen.begin_fill()
    for j in range(3):
        pen.forward(starWidth)
        pen.left(120)
    pen.end_fill()

    pen.up()
    pen.setpos(x,y + starWidth/2)
    pen.down()
    
    pen.begin_fill()
    for j in range(3):
        pen.forward(starWidth)
        pen.left(-120)
    pen.end_fill()

turtle.done()
