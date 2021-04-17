class House:
    def __int__ (self, address, x, y, width, building_color, roof_color, chimney, double_doors, num_windows):
        self.address = address
        self.x = x
        self.y = y
        self.width = width
        self.building_color = building_color
        self.roof_color = roof_color
        self.chimney = chimney
        self.double_doors = double_doors
        self.num_windows = num_windows
        self.sytle = ("Arial", int(width/4), "bold")

    def draw(self, pen):
        pen.up()
        pen.setpos(self.x, - self.width/2, self.y  - self.width/2)
        pen.down()
        pen.fillcolor(self.building_color)

        self.draw_house_base(pen)
        self.draw_chimney(pen)
        self.draw_roof(pen)
        self.write_street_address(pen)

    def draw_house_base(self, pen):
        pen.begin_fill()
        for i in range(4):
            pen.forward(self.width)
            pen.left(90)
        pen.end_fill()

    def draw_chimney(self, pen):
        if self.chimney:
            chimney_width = self.width * .2
            chimney_height = chimney_width * .3
            pen.up()
            pen.setpos(self.x - self.width * .4, self.y + self.width * .7)
            pen.down()
            pen.fillcolor(self.building_color)
            pen.begin_fill()
            for i in range(4):
                if i % 2 == 0:
                    pen.forward(chimney_width)
                else:
                    pen.forward(chimney_height)
                pen.left(90)
            pen.end_fill()

        def draw_roof(self, pen):
            roofWidth = self.width * 1.2
            pen.up()
            pen.setpos(self.x - roofWidth/2, self.y + self.width/2) 
            pen.down()
            pen.fillcolor(self.roof_color)
            pen.begin_fill()     
            for i in range(3):
                pen.forward(roofWidth)
                pen.left(120)
            pen.end_fill()

        def write_street_address(self, pen)
        pen.up()
        pen.setpos(self.x - self.width * .7, self.y - self.width * 1.1) 
            pen.down()
            pen.write(self.address, font = self.sytle)

        

