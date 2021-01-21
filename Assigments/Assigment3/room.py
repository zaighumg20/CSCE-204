# Author Talha Gill

#Room Width
RoomWidth = float(input("Enter your Room Width:"))

#Room Length
RoomLength = float(input("Enter your Room Length:"))

#Room Height
RoomHeight = float(input("Enter your Room Height:"))

#Room finishing cost
#Roomfinishingcost = float(input("Enter your Room finishingcost: "))

Finishingcost = (RoomWidth * 4) * 4  + ( RoomLength * 4) * 4 + (RoomHeight * 4)  * 4 

print(f"Room finishing cost: ${Finishingcost}")