#Author : Talha Gill
#import bird class
from bird import Bird

#create array 
lst = []
#append 4 objects of bird in array
lst.append(Bird("Cardinal","Red","Safflower seeds","These red birds love to come to your feeder."))
lst.append(Bird("Baltimore Oriole","Orange and Black","Oranges and Jelly","A beautiful orange songbird, and the state bird of Maryland"))
lst.append(Bird("Robin","Orange/Red Breast","Worms","They are beautiful singers. You will see them on lawns since morning."))
lst.append(Bird("Goldfinch","Yellow and Black","Nyjer Seed","Tiny beautiful birds with a pretty song"))

print("Bird Program!!!")
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