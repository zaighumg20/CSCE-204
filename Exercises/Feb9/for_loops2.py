# Get grades from a user (how many they want)
# sum them adn calculate the average


print("Grades Program ")

NumGrades= int(input("How many grades: "))
gradeTotal = 0

#Loop through and ask for the grades
for i in range(1,NumGrades + 1): 
    gradeTotal += int(input(f"Enter Grade {i}: "))


average = gradeTotal /NumGrades
print(f"Average is {average}" )

#print(f"Average is {round{average,1}" )