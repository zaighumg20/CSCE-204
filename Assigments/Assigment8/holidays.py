#Author: Talha Gill

#import date from datetime library
from datetime import date

#save holidays in dictionary
#holiday is key and date is value
holidays = {
            'Valentines Day':date(2021,2,14),'St. Patricks Day':date(2021,3,17),
            'Easter':date(2021,4,4),'Memorial Day':date(2021,5,31),
            'July 4th':date(2021,7,4),'Labor Day':date(2021,9,6),
            'Thanksgiving':date(2021,11,25),'Christmas':date(2021,12,25)
            }

#loop to iterate through holidays
#and store key values in holiday and Date variable
for holiday,Date in holidays.items():
    
    #if date is passed
    if date.today() > Date:
        print(holiday,' - ',Date.strftime("%m/%d/%y"),' Passed')
    #if date is today
    elif date.today() == Date:
        print(holiday,' - ',Date.strftime("%m/%d/%y"),' TODAY!')
    #if next holiday within 30 days
    elif (Date - date.today()).days <= 30:
        print(holiday,' - ',Date.strftime("%m/%d/%y"),' only ',(Date-date.today()).days,' days left')
    #else print simply holiday and date
    else:
        print(holiday,' - ',Date.strftime("%m/%d/%y"))

    
        
            

    
        
            