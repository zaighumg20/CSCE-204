import turtle
turtle.bgcolor("skyblue")
turtle.setup(500,500)


# setup pen
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("red")
pen.hideturtle()


# get the u- hual size
size = turtle.numinput("U-Haul" , "Size (1-10) : " , 4,1,10)

UHaulWidth = size * 50
boxWidth = UHaulWidth * .8
CabWidth = UHaulWidth - boxWidth
boxHeight = UHaulWidth / 2
Cabheight = boxHeight * .6
tireRadius = UHaulWidth * .1

# draw the UHaul Bdoy
pen.up()
pen.setpos(-UHaulWidth/2,0)
pen.down()
pen.begin_fill()
pen.forward(UHaulWidth)
pen.left(90)
pen.forward(Cabheight)
pen.left(90)
pen.forward(CabWidth)
pen.right(90)
pen.forward(boxHeight - Cabheight)
pen.left(90)
pen.forward(boxWidth)
pen.left(90)
pen.forward(boxHeight)

#draw left tire
pen.up()
pen.setheading(0)
pen.setpos(UHaulWidth/4, -tireRadius/2)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(tireRadius)
pen.end_fill()

 #draw right tire
pen.up()
pen.setheading(0)
pen.setpos(-UHaulWidth/4, -tireRadius/2)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(tireRadius)
pen.end_fill()

turtle.done()
