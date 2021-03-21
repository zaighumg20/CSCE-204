import turtle
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(5)
pen.hideturtle()

smileRadius = 30


def draw_smiley(x,y):
    draw_head(x,y)
    draw_eye(x - smileRadius/3,y)
    draw_eye(x + smileRadius/3,y)
    draw_mouth(x - smileRadius/2.5,y - smileRadius/3)

def draw_head(x,y):
    pen.up()
    pen.setpos(x,y - smileRadius)
    pen.down()
    pen.begin_fill()
    pen.fillcolor("yellow")
    pen.circle(smileRadius)
    pen.end_fill()

def eye(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    pen.fillcolor("black")
    pen.circle(smileRadius/11)
    pen.end_fill()

turtle.onscreenclick(draw_smiley)

turtle.done()