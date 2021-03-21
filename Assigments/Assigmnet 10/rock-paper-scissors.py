#Author: Talha Gill



import random

#play game function 
def play_game(player1_choice,comp_choice):
    #if choice of player and human i same then return 0
    if player1_choice == comp_choice:
        return 0
    #if cplayer 1 wins then return 1
    if player1_choice == "r" and comp_choice == "s" or player1_choice == "p" and comp_choice == "r" or player1_choice == "s" and comp_choice == "p":
           return 1
      #else return 2 when computer wins
    else:
        return 2
    
#function to get choice of a player
def get_players_choice():
    #take input from player
    choice = input('Enter (R)ock, (P)aper, or (S)cissors: ').lower()
    #if it's valid choice then return choice
    if choice == "r" or choice == "p" or choice == "s":
        return choice
    #else return false
    else:
        return False
    
#function to get computer's choice is randomly
def get_comp_choice():
    # llst of all 3 choices
    choices=["r","p","s"]
    #get random chouce using random choice
    comp_choice = random.choice(choices)
    #print computer's choice
    print('Computer choose: ',comp_choice)
    #retur  computer choice
    return comp_choice


#main function
print('Welcome to Rock Paper Scissors ')
#initially count of ties,player and computer is 0 
ties=0
player_wins=0
comp_wins=0

#infinitte loop until user pres q 
while True:
    #take choice from user
    choice = input('(P)lay or (Q)uit: ').lower()
    #if player enters p then play the game
    if choice=="p":
        #take input turn of a player
        choice1 = get_players_choice()
        #while loop until it's valid turn
        while choice1 == False:
            choice1 = get_players_choice()
            
        #take choice of a computer
        choice2 = get_comp_choice()
        #Call of play_game function and store result  
        result = play_game(choice1,choice2)
        
        #if result i 0 it means tie
        if result==0:
            print('Tie')
            ties+=1        
        #if result is 1 it means player won
        elif result == 1:
            print('You won!')
            player_wins+=1
        #else computer wins
        else:
            print('The computer won!')
            comp_wins+=1

   #if choice is q then quit the program 
    elif choice=="q":
        break
    #if print invalid command
    else:
        print('Inavlid command')
        
print('You won ',player_wins,' rounds')
print('The computer won ',comp_wins,' rounds')
print('You tied ',ties,' rounds')

        