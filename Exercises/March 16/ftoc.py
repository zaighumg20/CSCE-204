"""
Make a fuction called fahr_to_cells(farenheit) that returns celsius
Make a fuction called cels_to_fahr(celsius) that returns fahrenheit
Make a fuction called miles(miles) that returns kilometers
Make a fuction called kilo(kilo) that returns miles
""" 

def fahr_to_cells(farenheit):
    celsius = (farenheit - 32 ) * 5/9
    return celsius


def cels_to_fahr(celsius):
    farenheit = celsius * 9/5 + 32
    return farenheit

def miles_to_kilo(miles):
    kilometers = miles * 1.690934
    return kilometer

def  kilo_to_miles(kilo):
    kilometers = miles * 0.621371
    return miles

print('''Conversion Program'')
)
comnmand = int(input(f " " "
    Enter Type of conversion:
    1.Fahrenheit
    2.Celsius
    3.Miles to kilometer
    4.Kilometers to miles
    " " " ))

if command < 1 or commmand > 4:
    print("Invalid command")
else:
    value = float(input("Enter value"))

    if command ==1:
        result = fahr_to_cells(value)
        print(f"{value}F = {result} C")
    elif command ==2:
        result = cels_to_fahr(value)
        print(f"{value}C = {result} F")
    elif command ==3:
         result = miles_to_kilo(value)
        print(f"{value}Miles = {result} Kilo")
    elif command ==4:
         result = kilo_to_miles(value)
        print(f"{value}kilo = {result} Miles")
