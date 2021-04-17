from question import Question
import random

def get question():
    questions = []

with open('questions.txt') as file:
    for line in file:
        data = line.split(',')
        prompt = data[0].strip()
        answer1 = data[1].strip()
        answer2= data[2].strip()
        answer3 = data[3].strip()
        answer4= data[4].strip()
        correct_ans  = int(data[5]. stip())
        question = Question(prompt, answer1, answer2, answer3, answer4, correct_ans)

    return questions
questions = get_questions()

print("Trivia Game")

while True:
    command = input("(P)lay, or (Q)uit: ").strip().lower()

    if command == "q":
        break
    elif command != "p":
        print("Invalid input")
        continue

    question = random.choice(questions)
    print(question.prompt)
    question.dispaly_answer()
    user_ans = int(input("Enter numrical answer: "))

    if question.correct_answer == user_ans - 1:
        print("Nice!")
    else:
        print("Wrong!")
        
print("Goodbye")