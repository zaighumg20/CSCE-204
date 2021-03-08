toys = ["fish", "monkey", "ant", "burgers","batman" ]

print("Welcome to our toy Store")

while True:
    command = input("(L)ist, (A)dd, (R)emove, or (Q)uit: "). lower().strip()
    if command == "q":
        break
    elif command == "l":
        for i in range(len(toys)):
            print(f"{i +1}. {toys[i]}")
    elif command == "a":
        #ask the user for a toy 
        # if they entered something other than white space, append it to the list
        toy = input("Enter toy name: ").strip()

        if (toys != "" and (toys in toys) == False):
            toys.append(toy)
        else:
            print("Invalid toy name, either empty or already in the list")
    elif command == "r":
       toy = input("Enter toy name: ").lower().strip()

       if toy in toys:
           toys.remove(toy)  
    else:
        print("Invalid input, try again.")

    


print("GoodBye")
