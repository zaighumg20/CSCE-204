from datetime import date, time, datetime

todayDate = date.today()
print(todayDate.strftime("%m/%d/%y"))
print(todayDate.strftime("%A,%B,%w,%Y"))
print(todayDate.strftime("%B %d:%A, Year: %y"))


todaysDateTime = datetime.now()
print(todaysDateTime.strftime("%B %d, %Y, %I:%M %p"))



halloween = date(2022,10, 31)
metting = time(14, 30)
appointment = datetime(2021, 3 , 14 , 13, 59)

birthdayInput= input("Enter Birthday (MM/DD/YYYY): ").strip()
birthday = datetime.strptime(birthdayInput, "%m/%d/%Y")
print("Your birthday: " + birthday.strftime("%A %B %d, %Y"))



# how long till yur appt
days = (appointment - datetime.now()).days
print(f"You have {days} till your appointment")