#create an array of friends from the file
def get_friends():
    friends =[]

        #populate array with friends from file
    with open("friends.txt") as file:
        for line in file:
            friend=line.replace("\n", "")  
            friend.append(friends)
        
    return friends


#get friends, loop through and display them
chums= get_friends()


print("My best friends!")

#loop through and display list of friends in format: 1. Adam
for i in range(len(chums)):
    print(f"{i+1}. {chums[i]}")


