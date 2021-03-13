import turtle
import random
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()


def set_random_position():
    x = random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2))
    y = random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/2))

    pen.up()
    pen.setpos(x,y)
    pen.down()

def draw_square():
    set_random_position()


    length = 50

    for i in range (4):
        pen.forward(length)
        pen.left(90)


def draw_triangle():
    set_random_position()
    length = 50

    for i in range (3):
        pen.forward(length)
        pen.left(120)

def draw_star():
    set_random_position
    length = 50
    
    for i in range(3):
        pen.forward(length)
        pen.left(120)

    pen.up()
    pen.setheading(90)
    pen.forward(length/2)
    pen.down()


    for i in range (3):
        pen.forward(length)
        pen.right(120)

    draw_square
    draw_triangle
    draw_star

    for i in range(10):
        choice = random.randint(0,2)


        if choice == 0:
            draw_square()
        elif choice ==1 :
            draw_triangle
        elif choice ==2:
            draw_star()

turtle.done()