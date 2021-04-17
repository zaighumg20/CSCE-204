class Question:
    def __init__(self, prompt, answer1, answer2, answer3, answer4, correct_answer):
            self.prompt = prompt
            self.correct_answer = correct_answer
            self.answer = (answer1, answer2, answer3, answer4)

    #loop through answer and display them like: 1. crustacean, 2. 
    def dispaly_answer(self):
        for i in range(len(self.answers)):
            print(f"{i+1}. {self.answers[i]}")