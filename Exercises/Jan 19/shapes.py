import turtle
turtle.bgcolor("skyblue")

pen = turtle.Turtle()
pen.pensize(5)
pen.speed(0)
pen.color("purple")

# square
pen.forward(100)
pen.begin_fill()

pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)



#triangle
pen.up()
pen.setpos(-200,100)
pen.down()
pen.fillcolor("green")
pen.begin_fill()
pen.setheading(0)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.end_fill()

#triangle
pen.up()
pen.setpos(-200,-100)
pen.down()
pen.setheading(0)
pen.fillcolor("blue")
pen.begin_fill()
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.end_fill()


#circle
pen.up()
pen.setpos(-200,-200)
pen.down()
pen.fillcolor("red")
pen.circle(30)

turtle.done()