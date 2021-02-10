# Author: Talha Gill




import turtle
turtle.bgcolor("pink")
turtle.setup(500,500)

#setup pen
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("white")
size = 200


Housebase = size * .30


#set intial position to center
pen.up()
pen.setpos(-Housebase/5, -size/2)
pen.down()

# draw the base
pen.begin_fill()
pen.fillcolor("orange")
for i in range(4):
    pen.forward(Housebase)
    pen.left(90)
pen.end_fill()

#draw  traingle 
pen.up()
pen.setpos(-Housebase/2, -size/2 + Housebase)
pen.down()

# draw large triangle
pen.begin_fill()
pen.fillcolor("purple")
for i in range(3):
    pen.forward(Housebase + 33 ) 
    pen.left(120)
pen.end_fill()

#############

#plant position  
pen.up()
pen.setpos(Housebase + 16, -size/2)
pen.down()

#trunk
pen.begin_fill()
pen.fillcolor("brown")
for i in range(4):
    pen.forward(Housebase/3)
    pen.left(90)
pen.end_fill()

#trunk
pen.up()
pen.setpos(Housebase + 27, -size/2 + 14 )
pen.down()

#plant
pen.begin_fill()
pen.fillcolor("green")
pen.circle(Housebase/3.5)
pen.end_fill()


#sun
pen.up()
pen.setpos(-Housebase*2.85, size*.69)
pen.color("yellow")
pen.down()
pen.begin_fill()
pen.fillcolor("yellow")
pen.circle(Housebase/5.5)
pen.end_fill()

#rays
pen.up()
pen.setpos(-Housebase*2.85,size*.75)
pen.color("yellow")
pen.down()
for i in range (12):
    pen.forward(25)
    pen.setpos(-Housebase*2.85, size*.75)
    pen.down()
    pen.left(30)






turtle.done()