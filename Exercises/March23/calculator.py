#ask
#if they enter
def getPrice():
    while True:
        try:
            price = float(input("Enter Price: "))
            return price
        except ValueError:
            print("Sorry, that is not a valid number.")
        

#ask the user to enter a quantity
# if they enter
def getQuantity():
    while true:
        try:
            quantity = int(input("Enter Quantity"))
            return quantity
        except ValueError:
            print("Sorry, that is not valid whole number.")

#Calculator program
print("Our cost calculator")
price = getPrice()
quantity = getQuantity()
total = quantity * price * 1.07
print(f"Your total is ${round(total,2)}")