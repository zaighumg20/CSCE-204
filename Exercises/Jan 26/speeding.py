print("Police Program")
print ("Your have been pulled over")

speed  = float(input("Enter Speed "))



if speed >=100:
    print = "Go to jail"
elif speed >=90:
    print = "Big Ticket"
    ticketPrice = (speed - 70) * 50
    print(f"Ticket Price ${round(ticketPrice,2)}")
elif speed >=80:
    print = "Ticket"
elif speed >=70:
    print = "Warning"
elif speed > 50:
    print("good")
else:
 print("Too slow")