toys = {
    "doll" : 10.99,
    "truck" : 5.60,
    "car" : 3.50,
    "books" : 7.20

}

# add an item to your dictionary
toys["unicorn"] = 9.60

#loop through and display toys
for toy in toys:
    print(f"{toy}: ${toys[toy]}")


#ask for a toy and display the price
toyName = input("Enter toy name: ").strip().lower()

if toyName in toys:
    toyPrice = toys[toyName]
    Print(f"{toyname")
toyPrice = toys[toyName]
print(f"{toyName} costs ${toyPrice}")   

