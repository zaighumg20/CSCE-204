# Author: Talha Gil
# Create shape base on user input
import turtle
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.pensize(2)

# ask the user for the shape they want to draw
shape = turtle.numinput("shapes", "How many shapes whould you like")

shape =turtle.textinput("shapes", "Enter shapes( circle, square, triangle, or cross")



#shapes
shapesize = 50
pen.up()
pen.setpos(-100,0)
pen.down()
if shape == "square":
    for i in range(4):
        pen.forward(shapesize)
        pen.left(90)
elif shape == "triangle":
    #draw a triangle
    for i in range(3):
        pen.forward(shapesize)
        pen.left(120)
elif  shape == "star":
#right side of triangle
    for i in range(3):
        pen.forward(shapesize)
        pen.left(120)
    #upside down triangle
    for i in range(3):
        pen.forward(shapesize)
        pen.right(120)

'''
    pen.up()
pen.setpos(-50,0)
pen.down()
elif shape == "square":
    for i in range(4):
        pen.forward(shapesize)
        pen.left(90)
        pen.end_fill()
pen.up()
    pen.setpos(0,0)
    pen.down()
elif shape == "triangle":
    pen.up()
    pen.begin_fill()

    for i in range(3):
        pen.forward(shapesize)
        pen.left(120)
    pen.end_fill()
    pen.up()
    pen.setpos(50,0)
    pen.down()
    #right side of triangle
elif  shape == "star":
    for i in range(3):
        pen.forward(shapesize)
        pen.left(120)
    pen.up()
    pen.sety(25)
    pen.down()
    #upside down triangle
    for i in range(3):
        pen.forward(shapesize)
        pen.right(120)
        pen.up()
pen.setpos(100,0)
pen.down()
pen.up()
pen.setpos(100,0)
pen.down()



#First line 
elif shape == "cross":
    for i in range(1):
        pen.forward(shapesize)
        pen.up()
        pen.backward(shapesize/2)
        pen.left(90)
        pen.forward(shapesize/2)
        pen.down()
        pen.right(180)
        pen.forward(shapesize)

         pen.up()
    pen.setpos(0,-shapesize/2)
    pen.down()
    pen.circle(shapesize/2)
'''''



























turtle.done()
