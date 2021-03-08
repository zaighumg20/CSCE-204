WeekDays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday")

#loop through and dispaly items in the tuple
counter = 0 

for day in WeekDays:
    if counter == len(WeekDays) - 1:
        print(f"{day}" )
    else:
        print(f"{day}," ,end="") #prints on the line
    counter +=1