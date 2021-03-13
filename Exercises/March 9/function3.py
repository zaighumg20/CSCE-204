def factorial():
    num = int(input("Enter number: "))
    answer = 1

    #Error Invalid Input
    if num <1:
        print("Invalid number")
        return

    for i in range (1, num +1 ):
        answer *= i

    print(f"{num} ! = {answer}")


def power():
    base = int(input("Enter base: "))
    exp = int(input("Enter exponent:"))
    answer= 1

    if base < 1 or exp < 1:
        print("Invalid input")
        return
    
    # loop through and calculate ansr, then display it
    for i in range (exp):
        answer *=base
    
    print(f"{base}^{exp} = {answer}")

power()
def sum():
    num=int(input("Enter number: "))
    answer= 0

    for i in range(1, num + 1):
        answer = 0
    print(f" Sum of 1... {num} = {answer}")
# program 
print("Welcome to Math!")
while True:
    command = input("Compute (F)actorial, (S)um, (P)ower, or (Q)uit: ").strip().lower()

    if command =="q":
        break
    elif command =="f":
        factorial()
    elif command == "p":
        power()
    elif command =="s":
        sum()
    else:lower
    print("Invalid input")

print ("Goodbye")