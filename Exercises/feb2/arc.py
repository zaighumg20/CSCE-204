import turtle
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.pensize(2)

# draw grid
pen.up()
pen.setpos(-turtle.window_width()/2,0)
pen.down()
pen.forward(turtle.window_width())

# draw a grid vertical line
pen.up()
pen.setpos(0,turtle.window_height()/2)
pen.setheading(-90)
pen.down()
pen.forward(turtle.window_height())


# smile arc

smileRadius = 100
"""
pen.up()
pen.setpos(-smileRadius,0)
pen.down()
pen.setheading(-60)
pen.circle(smileRadius,120)
"""
# from arc
pen.up()
pen.setpos(0,0)
pen.down()
pen.setheading(60)
pen.circle(-smileRadius,120)




turtle.done()
