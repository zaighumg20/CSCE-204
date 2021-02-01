# Talha Gill

print("      ***Welcome to Talha's Book Store*** ") 

do = input("What would you like to do? (V)iew or (O)rder?: ") .lower().strip()

# V for View
if do >= "V":
    print(""" Our catalouge consists of:
    - 1984 by George Orwell 
    - The help by Kathryn Stockett
    - Gone with the wind by Margar Mitchell
    - The fellowship of the Ring by J.R.R. Tolkien """)
# O for order 
if do >="O":
    bookName = input("Enter book name: "). lower(). strip()
elif bookName >= "1984":
    print("You can buy 1984 for $9.99 ")
elif bookName >= "The Help" or "the help":
     print("You can buy The Help for $7.59 ")
elif bookName >= "Gone with the Wind" or "gone with the wind":
     print("You can buy Gone with the Wind for $8.50 ")
elif bookName >= "The Fellowship of the Ring" or "the fellowship of the ring":
     print("You can buy The Fellowship of the Ring for $10.11 ")