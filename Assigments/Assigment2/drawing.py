import turtle
turtle.bgcolor("light blue")

pen = turtle.Turtle()
pen.pensize(6)
pen.speed(0)

#hand
pen.up()
pen.setpos(-210,50)
pen.down()
pen.fillcolor("dark red")
pen.begin_fill()
pen.forward(400)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(400)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.end_fill()

#belly
pen.up()
pen.setpos(9,-190)
pen.down()
pen.fillcolor("dark red")
pen.begin_fill()
pen.circle(130)
pen.end_fill()

#ear 1
pen.up()
pen.setpos(50,190)
pen.down()
pen.fillcolor("dark red")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

#ear 2
pen.up()
pen.setpos(-40,190)
pen.down()
pen.fillcolor("dark red")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

#head
pen.up()
pen.setpos(5,50)
pen.down()
pen.fillcolor("dark red")
pen.begin_fill()
pen.circle(80)
pen.end_fill()

#leg 1
pen.up()
pen.setpos(60,-200)
pen.down()
pen.fillcolor("dark red")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

#leg 2
pen.up()
pen.setpos(-60,-200)
pen.down()
pen.fillcolor("dark red")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

#eye 1
pen.up()
pen.setpos(30,140)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

#eye 2
pen.up()
pen.setpos(-30,140)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

#mouth
pen.up()
pen.setpos(-20,110)
pen.down()
pen.fillcolor("orange")
pen.begin_fill()
pen.forward(50)


turtle.done()