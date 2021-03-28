while True:
try:    
    number = int(input("Enter number: "))
except ValueError:
    print("Sorry you did not enter a valid whole number.")