from bird import Bird

#function to load birds from file
def load_birds():
    
    file = open("birds.txt","r")
    #if file opened successfully
    for obj in file:
        #split the line by # character
        name,color,food,desc = obj.split('#')
        #apeend object in list
        lst.append(Bird(name,color,food,desc))    
    

print("              Bird Program   ")
#list of objects
lst=[]
#load birds
load_birds()

while True:
    choice = input("(L)ist all birds, get a birds (D)etails, or (Q)uit: ").upper()
    if choice == 'L':
        for obj in lst:
            obj.display()
    elif choice == 'D':
        bird_name = input('Enter bird Name: ')
        for obj in lst:
            if obj.is_match(bird_name):
                obj.display()
    elif choice == 'Q':
        print('Good bye!')
        break
    else:
        print('Invalid choice enter again!\n')