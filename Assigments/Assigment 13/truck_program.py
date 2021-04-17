#Author: Talha Gill

from truck import Truck
import turtle
from turtle import Screen
def draw_road():
   TURTLE_SIZE = 20
   screen = Screen()
   turtle.setup(575, 500)
   road = turtle.Turtle()
   road.penup()
   road.speed(1000)
   road.goto(TURTLE_SIZE/2 - screen.window_width()/2, -100)
   road.pendown()
   road.color("grey")
   road.begin_fill()
   road.forward(1500)
   road.left(90)
   road.forward(150)
   road.left(90)
   road.forward(1500)
   road.left(90)
   road.forward(150)
   road.end_fill()
   road.penup()
   road.left(90)
   road.setpos(TURTLE_SIZE/2 - screen.window_width()/2 , -35)
   for i in range(8):
      road.pendown()
      road.color("yellow")
      road.begin_fill()
      road.forward(100)
      road.left(90)
      road.forward(10)
      road.left(90)
      road.forward(100)
      road.left(90)
      road.forward(10)
      road.end_fill()
      road.penup()
      road.left(90)
      road.forward(200)

def draw_trucks():
   t = Truck(-50, 10, 40, "blue", True, False)
   t2 = Truck(-250, 10, 40, "green", False, True)
   t3 = Truck(120, 10, 40, "pink", False, True)
   pen = turtle.Turtle()
   pen.speed(1000)
   t2.draw(pen)
   pen = turtle.Turtle()
   pen.speed(1000)
   t.draw(pen)
   pen = turtle.Turtle()
   pen.speed(1000)
   t3.draw(pen)

if __name__ == "__main__":
   draw_road()
   draw_trucks()

turtle.done()