# Author: Talha Gill

import turtle
turtle.bgcolor("grey")
turtle.setup(500,500)

# setup pen
pen = turtle.Turtle()
pen.hideturtle()
size = turtle.numinput("olympic rings" , "Size (1-10) : " , 5,1,10)
circleRadius =size * 10

pen.pensize(size)

#draw the black circle
pen.up()
pen.color("black")
pen.setpos(0, circleRadius)
pen.setheading(0)
pen.down()
pen.circle(circleRadius)

#draw the blue circle
pen.up()
pen.color("blue")
pen.setpos(circleRadius * -2.5 ,circleRadius)
pen.setheading(0)
pen.down()
pen.circle(circleRadius)

#draw the red circle
pen.color("red")
pen.up()
pen.setpos(circleRadius * 2.5 , circleRadius)
pen.setheading(0)
pen.down()
pen.circle(circleRadius)

# draw gold circle
pen.up()
pen.color("gold")
pen.setpos(circleRadius * - 1.25, circleRadius * -.05)
pen.setheading(0)
pen.down()
pen.circle(circleRadius)

# draw ring
pen.up()
pen.color("green")
pen.setpos(circleRadius * 1.25, circleRadius * -.05)
pen.setheading(0)
pen.down()
pen.circle(circleRadius)


turtle.done()