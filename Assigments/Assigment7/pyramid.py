# Author :Talha Gill


import turtle
turtle.bgcolor("pink")
pen = turtle.Turtle()
pen.speed(0)



colors=[]
pyramidSize=int(turtle.numinput("Pyramid","Enter Height",5,1,10))

for i in range(pyramidSize):
    color=turtle.textinput("Pyramid","Enter color of row " + str(i+1))
    color=color.lower()
    colors.append(color)

x=-10
if(pyramidSize>6):
    p=10
    o=15
    u=30
    t=30
if(pyramidSize<=6):
    p=17
    o=25
    u=45
    t=50
if(pyramidSize<=3):
    p=27
    o=40
    u=70
    t=80

y=pyramidSize*10
for rows in range(pyramidSize):
    
    pen.up()
    pen.setpos(x,y)
    pen.fillcolor(colors[rows])
    pen.begin_fill()
    pen.down()
    z=x

    for col in range(rows+1):
        pen.setpos(z,y)
        for i in range(3):
            pen.forward(t)
            pen.left(120)
            z=z+p
    pen.end_fill()
    x=x-o
    y=y-u

pen.hideturtle()
turtle.done()