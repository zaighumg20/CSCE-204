import turtle
turtle.bgcolor("pink")
turtle.setup(500,500)

#setup pen
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("white")
pen.hideturtle()
pen.speed(0)

size = 200
#ask he user 
shape = turtle.textinput("shapes", "Enter Shape:").lower() .strip()

#center in the screen
pen.up()
pen.setpos(size/-2, -size/2)
pen.down()


if shape == "square":   
    for i in range(4):
        pen.forward(size)
        pen.left(90)
elif shape == "triangle":
#draw a triangle
    for i in range(3):
        pen.forward(size)
        pen.left(120)
elif  shape == "star":
#right side of triangle
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.up()
    pen.sety(0)
    pen.down()

#upside down triangle
    for i in range(3):
        pen.forward(size)
        pen.right(120)

turtle.done()