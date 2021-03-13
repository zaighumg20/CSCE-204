#Author: Talha Gill


#function to convert a decimal number into binary
def decimalToBinary(num):
    #create result string to store result of a binary number
    result=""
    #loop until num is greater than 0
    while num>0:
        #add the remainder of num/2 at start of result
        result = str(num%2) + result
        #divide the number by 2
        num = int(num/2)
        
    #print the binary result
    print(result)
    
#function is used to convert a binary number into decimal
def binaryToDecimal(num):
    #result variable to store decimal number of a binary
    result=0
    #i is used for the power of 2 (position)
    i=0
    #loop until number is greater then 0
    while num>0:
        #find remainder of a number by dividing it to 10
        #then multiply it to 2 raised to the power of position
        result+=(num%10)*(2**i)
        #increment in position
        i+=1
        #divide the number by 1o
        num=int(num/10)
    
    #print decimal result
    print(result)

#main

print('Calculator')
#loop until user press Q
while True:
    #take input in choice
    choice = input('Convert from binary to decimal (BtD) or from Decimal to Binary (DtB), or (Q)uit:')
    
    #if user press btd then call the function binary to decimal
    if choice.upper() == 'BTD':
        number = int(input('Enter binary number: '))
        binaryToDecimal(number)
        
    #if user press dtb then call the function decimal to binary    
    elif choice.upper() == 'DTB':
        number = int(input('Enter decimal number: '))
        decimalToBinary(number)
    
    #if user press q then quit the program
    elif choice.upper() == 'Q':
        print('Goodbye')
        break
    
    #if choice is invalid
    else:
        print('Invalid command')
    