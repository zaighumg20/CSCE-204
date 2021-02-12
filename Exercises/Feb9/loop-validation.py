'''
while True:
    grade = float(input("Enter grade between 0 and 100: "))

    if grade >= 0 and grade <= 100:
       break # get out of the loop when the grade is valid
    else:
        print("Invalid grade, please enter a number in the range: 1-100")
'''
grade = float(input("Enter grade between 0 and 100: "))

while grade < 0 or grade > 100:
    print("Invalid grade, please enter a number in the range: 1-100")
    grade = float(input("Enter grade between 0 and 100: "))