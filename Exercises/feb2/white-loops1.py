userInput = input ("Do you want to say hello: "). strip().lower()

while userInput == "y":
    print("Hello")
    userInput = input ("Do you want to say hello again: "). strip().lower()



print("Goodbye")