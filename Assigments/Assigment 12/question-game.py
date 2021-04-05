#Author: Talha Gill

import random
FILE_NAME_TRIVIA = "trivia.txt"
FILE_NAME_SCORE = "score.txt"
 
# Reach each line of the file into a dictionary.  The dictionary will look like:
# Question -> Answer 
# We use a convert to bool method to convert "true" to True  
def getQuestions():
    questions = {}
    with open(FILE_NAME_TRIVIA) as file:
        for line in file:
            data = line.split(':')
            question = data[0].strip()
            answer = data[1].strip()
            questions[question] = convertToBool(answer)
        return questions

# Converts a string representation of a boolean to a Boolean
def convertToBool(answer):
    if answer == "true":
        return True
    else:
        return False

# Asks the user a random trivia question
# Gathers the users answer
# if their answer is the stored answer then return true (they won), otherwise return false
def playRound():
    question = random.choice(list(questions.keys()))
    userAns = input(f"True or False: {question} ").strip().lower()
    compAns = questions.get(question)

    if convertToBool(userAns) == compAns:
        return True
    else:
        return False

#Get the scores from file
def getScores():
    #open the file score.txt
    with open(FILE_NAME_SCORE) as file:
        #Read lines from file
        lines = file.readlines()
        #store played games,won_games and lost games
        played_games=int(lines[0].strip())
        won_games=int(lines[1].strip())
        lost_games=int(lines[2].strip())
        #return the games
        return [played_games,won_games,lost_games]

#function to update scores
def saveScores(scores):
    #open file in write mode
    with open(FILE_NAME_SCORE,"w") as file:
        #write scores statistics in file
        file.write(str(scores[0]) + '\n')
        file.write(str(scores[1]) + '\n')
        file.write(str(scores[2]) + '\n')
        

# Let's play the game
print("Welcome to our Trivia Game")

#get scores 
scores=getScores()
#display scores at start
print('Games Played:',scores[0])
print('Games Won:',scores[1])
print('Games Lost:',scores[2])

# Load all the questions from the file
questions = getQuestions()

# Loop as long as the user wants to keep playing
while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()
    
    # if they enter q, quit the game
    if command == "q":
        break
    # if they enter an invalid command, indicate that
    elif command != "p":
        print("Invalid command")
        continue
    
    #if round played then increment in rounds_played
    scores[0]+=1
    # otherwise play around, if playRound is true, they won
    if playRound():
        #if round won then increment in won games
        scores[1]+=1
        print("Yay, you got it!")
    else:
        #if round lost then increment in rount lost
        scores[2]+=1
        print("Sorry, incorrect")

#update scores in file
saveScores(scores)
#display updates score
print('Games Played:',scores[0])
print('Games Won:',scores[1])
print('Games Lost:',scores[2])
print("Goodbye")
