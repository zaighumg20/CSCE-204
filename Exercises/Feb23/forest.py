import turtle
turtle.bgcolor("pink")
turtle.setup(500,500)

#setup pen
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()



gridSize = int(turtle.numinput("Size", "Enter size: ",5, 1, 10))
widthPadding = turtle.window_width()/gridSize
padding = widthPadding * .1
width = widthPadding * .8



leafradius = width * .5/2
stumpradius = width * .2
stumpHeight = width * .5
stumpWidth = width * .2

for row in range(gridSize):
    x = - turtle.window_width()/2 + widthPadding/2 - stumpWidth / 2
    y = - turtle.window_height()/2 + padding + row * widthPadding


    for col in range(gridSize):
        pen.up()
        pen.setpos(x,y)

        # draw stump
        pen.color("sienna")
        pen.begin_fill()
        for i in range (4):
            if i % 2 ==0: #if Even
                pen.forward(stumpWidth)
            else:
                pen.forward(stumpHeight)
            pen.left(90)
        pen.end_fill()

        # 
        pen.color("forest green")
        pen.up()
        pen.setpos(x + stumpWidth/2, y + stumpHeight * .8)
        pen.down()
        pen.begin_fill()
        pen.circle(leafradius)
        pen.end_fill()

        x += widthPadding
















turtle.done()