from datetime import date

birthdays = {
    "Amy":  date(2021, 3, 22),
    "Bobby": date(2021,2, 10),
    "Jenny": date(2021, 5, 29),
    "Sammy": date(2021, 11, 21),
    "Jen":  date(2021, 10, 22), 
    "Liam" :date(2021, 3, 2),
    "Eric": date(2021, 6, 24), 
    "Stan":  date(2021, 3, 12)

}
closestBirthday = date(2021, 12, 31)
closestFriend = ""

for person in birthdays:
    birthday = birthdays[person]
    daysTillClosest = (closestBirthday - date.today()).days
    daysTillBirthday = (birthday - date.today()).days


    #birthday already passed
    if daysTillBirthday <0:
        continue #go to next time in list

    if daysTillBirthday < daysTillClosest:
        closestBirthday = birthday

print(f"Closest birthday is {closestFriend}: " + closestBirthday.strftime("%m/%d/%y"))