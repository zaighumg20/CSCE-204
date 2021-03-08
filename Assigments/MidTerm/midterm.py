#Author: Talha Gill


import turtle
turtle.speed(0)
turtle.penup()
turtle.setpos(-190,170)
turtle.penup()
pen = turtle.Turtle()
turtle.write("My Contact List: ",font=('courier',20))
pen.hideturtle()

fname=[]
lname=[]
genders=[]
numbers=[]
#validate if the length of first name is under 10
def validfname(name):
  if(len(name)<=10):
    fname.append(name)
    return 1
  return 0
#validate if the length of last name is under 10  
def validlname(name):
  if(len(name)<=10):
    lname.append(name)
    return 1
  return 0

leng=int(turtle.numinput('Contacts',"How many contacts you want to add: ",1))

for x in range(leng):
  while(True):
    name=turtle.textinput('First Name',"Enter the first name of  the " + str(x+1) +" person: ")
    if(validfname(name)):
      break
  
  while(True):
    name=turtle.textinput('Last Name',"Enter the Last name of  the " + str(x+1) +" person: ")
    if(validlname(name)):
      break
  
  gender=turtle.textinput('Gender',"Enter the gender of  the " + str(x+1) +" person: ")
  genders.append(gender)
  num=turtle.textinput('Person',"Enter the number of  the " + str(x+1) +" person: ")
  numbers.append(num)
#the following if's are used to adjust the size of stickman relative to the number of contacts
  
if(leng==1 or leng==2):
  move=-100
  fonts=15
  name=180
  side=160
  cir=60
  li1=80
  li2=60
  
if(leng==3):
  move=-130
  name=150
  fonts=10
  side=130
  cir=30
  li1=50
  li2=40
  
if(leng==4):
  move=-150
  fonts=8
  name=120
  side=100
  cir=25
  li1=40
  li2=30
  
if(leng==5):
  move=-150
  fonts=6
  name=100
  side=80
  cir=20
  li1=35
  li2=25
  
if(leng==6):
  move=-170
  fonts=5
  name=85
  side=65
  cir=15
  li1=30
  li2=20
#the following 5 lines of code is done to get the 1st stickman to the most left
pen.up()
pen.setpos(move,-20)
pen.down()
pen.speed(0)
#this for loop print the number of stickman as many as the contacts
for i in range(leng):
  #this if moves the other stickman to the left of the first one
  if(i!=0):
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(move,-20)
    pen.down()
    pen.speed(0)
  #these two if's checks the gender and change the color of stickman
  if(genders[i].lower()=="female"):
    pen.color("brown")
    
  if(genders[i].lower()=="male"):
    pen.color("black")
  #.setheading is a function that determines where the turtle head would move, at what angle, i.e. at 90 meaning up
  #.forward function moves the turtle to the given angle
  pen.circle(cir)
  pen.setheading(270)
  pen.forward(li1)
  pen.setheading(90)
  pen.forward(li2)
  pen.setheading(0)
  pen.forward(li2)
  pen.setheading(180)
  pen.forward(li2*2)
  pen.setheading(0)
  pen.forward(li2)
  pen.setheading(270)
  pen.forward(li2)
  pen.setheading(300)
  pen.forward(li2)
  pen.setheading(120)
  pen.forward(li2)
  pen.setheading(240)
  pen.forward(li2)
  if(genders[i].lower()=="female"):
    pen.setheading(0)
    pen.forward(li2)
  #this goto moves the turtle over the head of the stickman to print the information
  pen.up()
  pen.setpos(move,name-40)
  pen.pendown()
  #.write is a fucntion which is use to write text in the turtle
  pen.write(fname[i]+" "+lname[i],font=('Courier',fonts),align='center')
  #this goto moves the turtle  below the name to print the contact number
  pen.up()
  pen.setpos(move,side-40)
  pen.down()
  
  pen.write(numbers[i],font=('Courier',fonts),align='center')
  move=move+side
  pen.hideturtle()

  
  
turtle.done()