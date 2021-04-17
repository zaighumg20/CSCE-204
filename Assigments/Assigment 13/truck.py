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
       pen.up()
       pen.setpos(self.x, self.y)
       pen.pendown()
       pen.begin_fill()
       if self.xlong_bed:
          width = 370
       else:
          width = 320
       pen.forward(width)
       pen.left(90)
       pen.forward(50)
       pen.left(90)
       pen.forward(width)
       pen.left(90)
       pen.forward(50)
       pen.end_fill()

       # Below code for drawing window and roof
       pen.penup()
       pen.setpos(self.x + 50, self.y + 50)
       pen.pendown()
       pen.color(self.color)
       pen.begin_fill()
       pen.setheading(90)
       pen.forward(70)
       pen.setheading(0)
       pen.forward(100)
       pen.setheading(-90)
       pen.forward(70)
       pen.setheading(90)
       #########################3
       if self.extended_can:
         pen.setheading(90)
         pen.forward(70)
         pen.setheading(0)
         pen.forward(100)
         pen.setheading(-90)
         pen.forward(70)
         pen.setheading(90)
       ##################################
       

       # Below code for drawing two tyres
       pen.penup()
       pen.setpos(self.x + 100, self.y -10)
       pen.pendown()
       pen.color('#000000')
       pen.fillcolor('#000000')
       pen.begin_fill()
       pen.circle(20)
       pen.end_fill()
       pen.penup()
       pen.setpos(self.x + 300, self.y -10)
       pen.pendown()
       pen.color('#000000')
       pen.fillcolor('#000000')
       pen.begin_fill()
       pen.circle(20)
       pen.end_fill()


