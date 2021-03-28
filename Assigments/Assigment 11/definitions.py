
#Author: Talha Gill

#function to get definitions in dictionary
def getDictionary():
    #create empty dictionary
    definitions={}
    #try block
    try:
        #open "words.txt" file in reading mode 
        with open('words.txt') as file:
            #go thorugh each line of file
            for line in file:
                #replace newline chracter with empty chracter
                line=line.replace("\n","")
                #split word and definition
                word,definition=line.split(': ')
                #store definition as value and word as key
                definitions[word]=definition
       #return dictionary
        return definitions       
    #if file not found
    except:
        print('file \"words.txt\" is not found!')
        
#Function to get definition of a word
def getDefinition(definitions):
    #take input in word
    word=input('Enter word: ')
    #if word exist in definitions
    if word in definitions:
        #then print the definition
        print(definitions[word])
    #else print error message
    else:
        print('This word doesn\'t exist in dictionary')
        
#Function to display all words and definition
def displayDictionary(definitions):
    for word,definition in definitions.items():
        print(word,':',definition)
        
#main function definition
def main():
    #store dictionary of words and definition in dictionary named definitions
    definitions = getDictionary()
    
    #if definition has some lines
    if definitions:
        #then welcome into dictionary menu
        print('Welcome to our dictionary')
        
        #Loop until user quit
        while True:
            #take input in choice
            choice = input('Would you like to (V)iew, (D)efine, or (Q)uit:' ).lower()
            #if choice is v then display the dictionary
            if choice == 'v':
                displayDictionary(definitions)
            #if choice is d then display the definition of word
            elif choice == 'd':
                getDefinition(definitions)
            #if choice is q then quit and break the loop
            elif choice == 'q':
                print('Good bye')
                break
            #if choice is invalid print invalid choice
            else:
                print('Invalid choice')
#main
if __name__=='__main__':
    main()
