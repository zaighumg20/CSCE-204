#Author: Talha Gill


class Bird:
       
    def __init__(self, bird_type,color,food,description):
        self.bird_type = bird_type
        self.color = color
        self.food = food
        self.description = description
   
    def display(self):
        print("***",self.bird_type,"***")
        print("color:",self.color)
        print("food:",self.food)
        print(self.description,"\n")
    
    def is_match(self,bird_name):
        if bird_name == self.bird_type:
            return True
        else:
            return False
