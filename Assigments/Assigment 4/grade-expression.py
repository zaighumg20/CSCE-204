# Author: Talha Gill

import turtle

turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.pensize(2)



# ask the user for the their Grade
grade = turtle.numinput("Grades", "Enter Grade:")



headRadius = 200
pen.up()
pen.setheading(0)
pen.setpos(0,-headRadius)
pen.down()
pen.fillcolor("red")
pen.circle(headRadius)

#eye 1
pen.up()
pen.setheading(0)
pen.setpos(-headRadius/3, headRadius/10)
pen.fillcolor("black")
pen.begin_fill()
pen.down()
pen.circle(20)
pen.end_fill()

#eye 2
pen.up()
pen.setheading(0)
pen.setpos(headRadius/3, headRadius/10)
pen.fillcolor("black")
pen.begin_fill()
pen.down()
pen.circle(20)
pen.end_fill()

# smile arc

if grade >=80:
    pen.up()
    pen.setpos(-headRadius * .4, -headRadius *.4)
    pen.down()
    pen.setheading(-60)
    pen.circle(headRadius/2,120)
elif grade >=70:
    pen.up()
    pen.setpos(-headRadius*.4,-headRadius*.4)
    pen.down()
    pen.setheading(0)
    pen.forward(180)
elif grade <69:
    pen.up()
    pen.setpos(-headRadius*.4,-headRadius*.4)
    pen.down()
    pen.setheading(60)
    pen.circle(-headRadius/2,120)
pen.hideturtle()





turtle.done()