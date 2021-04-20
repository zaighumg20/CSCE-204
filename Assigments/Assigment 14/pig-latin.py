#Author: Talha Gill

#function to check a letter is vowel or not
def is_vowel(letter):
    #list of vowels
    vowels =['a','e','i','o','u']
    #if letter is vowel then return true
    if letter in vowels:
        return True
    #else return false
    else:
        return False
    
#function to convert word into pig-latin
def convert_to_pig_latin(word):
    #if first word is not vowel
    if not is_vowel(word[0]):
        #first letter of word
        first_letter = word[0]
        #convert into pig_latin
        word=word[1:]+"-"+first_letter+"ay"
    
    #if first word is vowel then just append "-hay"
    else:
        word+="-hay"
    
    #return word
    return word

#main function
def main():
    
    #loop until user quite
    while(True):
        #take input in choice 
        choice = input('(C)onvert or (Q)uit: ').lower()
        #if 'c' then convert word into latin
        if choice == 'c':
            word = input('Enter a word: ')
            print(word + " in pig-latin is "+ convert_to_pig_latin(word))
        #if 'q' then quite the program 
        elif choice == 'q':
            print('Goodbye')
            break
        #if invalid command then print messsage
        else:
            print('Invalid command')
            
#main
if __name__ == '__main__':
    main()