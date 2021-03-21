# gender =  or f
#length = l or s
#density = t or th

def gey_cut_cost(gender,length,density):
    price = 0


    #price based on gender
    if gender == "m":
        price+= 20
    else:
        price +=40
    #price based on length
    if length == "l":
        price += 10
    #price based on thinkness
    if density == "t":
        price +=15

# length = l or s
#density = t or th
#change = "l" or "d"
def     get_color_cost(length,density,change):
        basePrice = 100

        if length == "l":
            basePrice +=40

        if density == "t":
            basePrice +=60

        if change=="l":
            basePrice +=50

        return baseprice

print ("Salson Services")
print("Price estimation calculation")


gender= input("Gender (M)ale or (F)emale:").strip().lower()
hairLength = input("Length (L)long or (S)hort:").strip().lower()
hairDensity = input("Density (T)hicj or (TH)hin:").strip().lower()
hairCut = input("do you want your hair cut(Y)es or (N)o: ").strip(). lower()
hairColor= input("Do you want your hair colored (Y) or (N): ").strip().lower()


cost = 0 


if hairCut == "y":
    cost+= get_cut_cost(gender, hairLength,hairDensity)
if hairColor =="y":
    colorChange = input("Will you be going (L)ighter or (D)arker:").strip().lower()
    cost+= get_color_cost(hairLength, hairDensity, colorChange)

#amount for tax
cost *= 1.07

print (f"Your estimated total is $(round(cost,2)}")
