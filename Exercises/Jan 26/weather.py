print("What should you wear")

temp = float(input("Enter Temperature: "))
percip = input("Enter percip (R)ain, (S)now, (N)one: "). lower(). strip()

if temp <= 32 and precip == "n":
    print("Wear a warm jacket")
elif temp <= 32 and percip == "s" :
    print ("Wear a snow suit")
elif temp <= 50 and precip == "n" :
    print ("Wear a jacket")
elif temp <= 50 and precip == "r" :
    print ("Wear rain jacket") 
else:
    print("Sorry this app is not complete")

