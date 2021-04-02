import random

def get_score():
    with open("score.txt") as file:
        for line in file:
            return int(line)

        return 0 

#save the score to the file
def save_score(score):
    with open("score.txt") as file:
        file.write(f"{score}")

save_score(5)
myScore = get_score()
print(f"Your score is {myScore}")
def play_round():
    randNum = random.randint(1000,9999)
    sum = sum_digits(randNum)

    UserAnswer = int(input(f"Sum digits in {randNum}: "))

    if UserAnswer == sum:
        return True
    else:
        print(f"Sorry the sum should be {sum}")
        return False

def sum_digits(num):
    sum = 0 


    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10


    return sum

score = get_score()
while True:
command = input("(P)lay or (Q)uit: ".strip().lower()

    if command == "q":
        break
    elif command !="p":
        print(Invalid command")
        continue
    if play_round():
        score += 1
        print("YAY")
        
print("Goodbye")
save_score(score)
pritnt(f"Your current score is {score}")