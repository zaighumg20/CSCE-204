from house import House
import turtle
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

houses = []
houses.append(House("1 A street", -200, 0, 50, "medium aquamarine", "hot pink", True, True, 3))
houses.append(House("2 A street", 100, 0, 50, "burlywood", "cyan", True, False, 3))
houses.append(House("3 A street", 0, 0, 50, "medium orchid", "khaki", True, True, 3))
houses.append(House("4 A street", 100, 0, 50, "sandy brown", "aquamrine", False, True, 3))
houses.append(House("5 A street", 200, 0, 50, "light sky blue", "plum", True, True, 3)

for house in houses:
    houses.draw(pen)


turtle.done()   

