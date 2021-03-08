from datetime import date

birthdays = [
    date(2021, 3, 22), date(2021,2, 10), date(2021, 5, 29),
    date(2021, 11, 21), date(2021, 10, 22), date(2021, 3, 2),
    date(2021, 6, 24),  date(2021, 3, 12)

]
closestBirthday = date(2021, 12, 31)

for birthday in birthdays:
    daysTillClosest = (closestBirthday - date.today()).days
    daysTillBirthday= (birthday - date.today()).days


    #birthday already passed
    if daysTillBirthday <0:
        continue #go to next time in list

    if daysTillBirthday < daysTillClosest:
        closestBirthday = birthday
print("Closest birthady is: " + closestBirthday.strftime("%m/%d/%y"))