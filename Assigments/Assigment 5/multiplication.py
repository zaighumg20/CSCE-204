# Author  Talha Gill

import random
import sys


print("Welcome to our multiplcation Game")

while True:
    print('''
Shall we ask you a question (Y)es or (N)o?: '''
    , end='')

    sel = input("")

    if sel=='y' or sel=='Y':
        n1 = random.randint(1,50)
        n2 = random.randint(1,50)
        print(f"{n1}x{n2}= ", end='')
        guess = int(input(""))

        if (guess == int((n1*n2))):
            print("You got it!")
        else:
            print("Sorry, the correct answer is", int((n1*n2)) )
    elif sel=='n' or sel=='N':
        print("Goodbye")
        sys.exit(0)
  # Author  Talha Gill

import random
import sys


print("Welcome to our multiplcation Game")

while True:
    print('''
Shall we ask you a question (Y)es or (N)o?: '''
    , end='')

    sel = input("")

    if sel=='y' or sel=='Y':
        n1 = random.randint(1,50)
        n2 = random.randint(1,50)
        print(f"{n1}x{n2}= ", end='')
        guess = int(input(""))

        if (guess == int((n1*n2))):
            print("You got it!")
        else:
            print("Sorry, the correct answer is", int((n1*n2)) )
    elif sel=='n' or sel=='N':
        print("Goodbye")
        sys.exit(0)
    else:
        print("invalid selection")

