#Author:Talha Gill


import random
import turtle
turtle = turtle.Turtle()


# method to draw 10 rubics cube
def draw10():
    for i in range(10):
        size = random.randint(20, 100)

        # size of screen in my machine, can be different in other machines
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        draw_rubics_cube(x, y, size)




# method to draw a single square
def draw_square(x, y, width, color):
    global turtle
    turtle.up()
    turtle.setpos((x, y))
    turtle.down()
    turtle.setheading(90)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(width)
        turtle.rt(90)
    turtle.end_fill()

# method to draw 9 boxes in the form of rubics cube
def draw_rubics_cube(x, y, size):
    colors = ['red', 'blue', 'yellow', 'orange', 'green', 'white']
    (tempx, tempy) = (x, y)
    for i in range(3):
        tempx = x
        for j in range(3):
            col = random.randint(0,len(colors)-1)
            draw_square(tempx, tempy, size, colors[col])
            tempx += size
        tempy += size


draw10()
turtle.done()