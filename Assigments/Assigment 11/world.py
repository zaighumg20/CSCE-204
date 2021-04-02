#Author: Talha Gill


import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

color = ""
def getScene():
   items = []
   with open("scene.txt") as file:
      for line in file:
         item = line.replace("\n", "")
         items.append(item)
   return items

def drawTriangle(x, y, size):
   pen.up()
   pen.color(color)
   pen.fillcolor(color)
   pen.setpos(x,y)
   pen.down()
   pen.begin_fill()
   for i in range (3):
      pen.forward(size)
      pen.left(120)
   pen.end_fill()
   pen.setheading(0)


def drawUpsideDownTriangle(x, y, size):
   pen.up()
   pen.color(color)
   pen.fillcolor(color)
   pen.goto(x,y)
   pen.pendown()
   pen.begin_fill()
   for i in range (3):
      pen.forward(size)
      pen.left(240)
   pen.end_fill()
   pen.setheading(0)

def drawStar(x, width):
   global color
   color = "Yellow"
   drawUpsideDownTriangle(x, width/2, width)
   drawTriangle(x, 0, width)


def drawTree(x, width):
   global color
   color = "Green"
   drawTriangle(x, -10, width)
   drawTriangle(x, 5, width)
   drawTriangle(x, 20, width)

def main():
   items = getScene()

   x = -200
   for item in items:
      if item == "star":
         drawStar(x, 50)
         x += 70
      if item == "tree":
         drawTree(x, 50)
         x += 70


main()

turtle.done()