numGrades = int(input("Enter num grades: "))
sum = 0

#loop and gather grades
for i in range(numGrades):
    grade = float(input(f"Enter grade {i + 1}: "))
    
    while grade < 0 and 100:
        print("Invalid grade")
        grade = float(input(f"Enter grade {i + 1}: "))

    sum += grade

average = sum / numGrades
print(f" Average is: {average}") 