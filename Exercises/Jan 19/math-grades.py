#Author Talha Gill

#assignments
assigments = float(input("Enter your assignments: "))

#exercises
exercises = float(input("Enter your exercises: "))

#quizzes
quizzes = float(input("Enter your quizzes: "))

#midterm
midterm = float(input("Enter your midterm: "))


#final
final = float(input("Enter your final: "))

finalGrade = assigments * 0.25  + exercises * 0.10 + quizzes * 0.15 + midterm * 0.25 + final * 0.25
finalGrade =round(finalGrade, 1)

print(f"Your final Grade is {finalGrade}")