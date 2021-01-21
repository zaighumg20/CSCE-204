#Author Talha Gill
# Age predictor


age = float(input("Enter age: "))
decade = 10
futureAge = age + decade

print(f"""You are {age} year old.
In a decade you will be {futureAge} year old. """)
# / float division, will be precise in a deciaml
# // interger division, will cut off the decimal
# // round variable, decimal places..  round(3.75. 1)= 3.8
#pizza Party
numGuests = int(input("Enter Num Guest "))
slicesPerGuest = 2.5
totalSlices = numGuests * slicesPerGuest
numPizzas = totalSlices / 6
# numPizzas =math.ceil(numPizzas)
numPizzas = 36.5


# numPizzas =round(numPizzas,0)
print(f"""You are having {numGuests} to your party.
You will need {totalSlices} number of pizza slices and {numPizzas} pizzas.""")

#chicken
numEggs = 57
numCartons =numEggs // 12

print(f""" You need {numCartons} cartons of eggs.""")


#travelling
miles  = float(input("Enter miles you traveled"))
PriceperMiles =float(input("Enter price per miles"))
totalCost = round(miles * PriceperMiles,2)

print(f"you will be charged ${totalCost}")