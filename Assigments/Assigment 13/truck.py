class Truck:
    def __init__(self, x, y, height, color, extended_can, xlong_bed):
        self.x = x
        self.y = y
        self.height = height
        self.color = color
        self.extended_can = extended_can
        self.xlong_bed = xlong_bed
    def draw(self, pen):
       pen.color(self.color)
       pen.fillcolor(self.color)
       pen.penup()
       pen.setpos(self.x, self.y)
       pen.down()
       pen.begin_fill()
       if self.xlong_bed:
          width = 320
       else:
          width = 300
       pen.forward(width/2)
       pen.left(90)
       pen.forward(50/2)
       pen.left(90)
       pen.forward(width/2)
       pen.left(90)
       pen.forward(50/2)
       pen.end_fill()

       # Below code for drawing window and roof
       pen.penup()
       pen.goto(self.x + 25, self.y + 25)
       pen.pendown()
       pen.color(self.color)
       pen.begin_fill()
       pen.setheading(90)
       pen.forward(70/2)
       pen.setheading(0)
       pen.forward(100/2)
       pen.setheading(-90)
       pen.forward(70/2)
       pen.setheading(90)
       #########################3
       if self.extended_can:
         pen.setheading(90)
         pen.forward(70/2)
         pen.setheading(0)
         pen.forward(100/2)
         pen.setheading(-90)
         pen.forward(70/2)
         pen.setheading(90)
       ##################################
       

       # Below code for drawing two tyres
       pen.penup()
       pen.setpos(self.x + 50, self.y - 7)
       pen.pendown()
       pen.color('#000000')
       pen.fillcolor('#000000')
       pen.begin_fill()
       pen.circle(10)
       pen.end_fill()
       pen.penup()
       pen.setpos(self.x + 150, self.y -7)
       pen.pendown()
       pen.color('#000000')
       pen.fillcolor('#000000')
       pen.begin_fill()
       pen.circle(10)
       pen.end_fill()


