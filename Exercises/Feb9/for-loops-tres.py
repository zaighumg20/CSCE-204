import turtle
turtle.bgcolor("pink")
turtle.setup(500,500)

#setup pen
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("green")

pen.speed(0)
size = 200


smSize = size * .25
mdSize = size * .3
lgSize = size * .4
trunkSize = size * .15

#set intial position to center
pen.up()
pen.setpos(-trunkSize/2, -size/2)
pen.down()

#draw trunk
pen.begin_fill()
pen.fillcolor("brown")
for i in range(4):
    pen.forward(trunkSize)
    pen.left(90)
pen.end_fill()

#draw  traingle 
pen.up()
pen.setpos(-lgSize/2, -size/2 + trunkSize)
pen.down()

# draw large triangle
pen.begin_fill()
pen.fillcolor("green")
for i in range(3):
    pen.forward(lgSize)
    pen.left(120)
pen.end_fill()

#draw med traingle 
pen.up()
pen.setpos(-mdSize/2, -size/2 + trunkSize + lgSize/2)
pen.down()

# draw med triangle
pen.begin_fill()
pen.fillcolor("green")
for i in range(3):
    pen.forward(mdSize)
    pen.left(120)
pen.end_fill()

#draw med traingle 
pen.up()
pen.setpos(-mdSize/2, -size/2 + trunkSize + lgSize/2 + mdSize/2)
pen.down()

# draw med triangle
pen.begin_fill()
pen.fillcolor("green")
for i in range(3):
    pen.forward(mdSize)
    pen.left(120)
pen.end_fill()





turtle.done() 