# Author: Talha Gill
# Create shape base on user input
import turtle
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.pensize(2)

# ask the user for the shape they want to draw
shape = turtle.textinput("shapes", "Enter Shape:").lower() .strip()

# Ask the user for a color then set the fill color
color = turtle.textinput("Color", "Enter color").lower() .strip()

#  ask the user for a size between 1 and 10, abd adjust
shapSize =turtle.numinput("Size", "Enter Size",5,1,10)*20
shapesize = 200
pen.fillcolor(color)

if shape == "circle":
    pen.up()
    pen.setpos(0,-shapesize/2)
    pen.down()
    pen.begin_fill()
    pen.circle(shapesize/2)
    pen.end_fill()

elif shape == "square":
    pen.up()
    pen.begin_fill()

    for i in range(4):
        pen.forward(shapSize)
        pen.left(90)
    pen.end_fill()

elif shape == "triangle":
    pen.up()
    pen.setpos(-shapesize/2,-shapesize/2)
    pen.down()
    pen.begin_fill()    
        
    pen.forward(shapesize)
    pen.left(120)
    pen.forward(shapesize)
    pen.left(120)
    pen.forward(shapesize)
    pen.left(120)
    pen.forward(shapesize)

    pen.end_fill()
    
turtle.done()