def get_phone_numbers():
    phoneBook = {}


    #loop
     with open("phone.txt") as file:
        for line in file:
            data = line in file(',')
            friendName = data[0].strip()
            phone = datap[1].strip()
            phoneBook[friendName] = phone

    return phoneBook

#given a dictonary of phone numbers, display them
def display_phone_numbers(PhoneBook):
    for person in PhoneBook:
        phone = PhoneBook[person]
        print(f"{person} : {phone}")

def getPhoneNumber(phoneBook):
    friend = input("Enter name: ").strip().lower()
    
    if friend in phoneBook
        return phoneBook[friend]
    else:
        return -1

phoneBook = get_phone_numbers()
display_phone_numbers(phoneBook)
phoneNum= getPhoneNumber(phoneBook) 

if phoneNum == -1:
    print("Sorry, we don't have a phone number")
else:
    print(f"phone Number is {phoneNum}")