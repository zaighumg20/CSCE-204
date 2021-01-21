import turtle
turtle.bgcolor("blue")

# setup pen
pen = turtle.Turtle()
pen.pensize(5)

# House Body
pen.up()
pen.setpos(-100,-100)
pen.down()
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)

# House Roof
pen.up()
pen.setpos(-100,100)
pen.down()
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(120)
pen.forward(200)

# Door
pen.up()
pen.setpos(-25,-100)
pen.setheading(0)
pen.down()
pen.forward(50)
pen.right(90)
pen.forward(-100)
pen.right(90)
pen.forward(100)
pen.left(90)
pen.forward(100)

# Door Knob
pen.up()
pen.setup(-10,-30)
pen.setheading(0)
pen.down()
pen.forward(30)
pen.right(10)



turtle.done()

