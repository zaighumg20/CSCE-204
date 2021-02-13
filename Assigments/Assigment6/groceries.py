#Author: Talha Gill

print("Welcome to our grocery store")

print("The following Items are in the store:")
items = ["Apples", "Bananas", "Oranges", "Kiwis", "Grapes" ]

def store(list):
    check = False;

    for i in range(list.__len__()):
        print("-",list[i])
    i = 0
    product = input("What whould you like to order? ").lower().strip()



    for i in range(list.__len__()):
        if product == list[i].lower().strip() :
            x = list[i]
            print("We've ordered", product, "for you")
            list.remove(x)
            check = True
            break

    if check == False:
        print("Sorry we don't have any", product)



    print("Now the grocery store contains the following:")
    for items in list:
        i+=1
        print("-",items)
    print("GoodBye")

store(items)