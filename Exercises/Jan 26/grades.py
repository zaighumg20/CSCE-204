print("Caluclate Your Grade")

assigments = float(input("Assigments "))
quizzess = float(input("Assigments "))
midterm = float(input("midterm "))
final = float(input("Final "))
classGrade = assigments * .4 + quizzess * .1 + midterm *.25 + final * .25
letterGrade = "F"
print(f" Your grade is {round(classGrade,1 )} ")

if classGrade >=89.5:
    letterGrade = "A"
elif classGrade >=79.5:
    letterGrade = "B"
elif classGrade >=69.5:
     letterGrade = "C"
elif classGrade >=59.5:
      letterGrade = "D"
else:
      letterGrade ="F"
print(f"letterGrade is {letterGrade}")