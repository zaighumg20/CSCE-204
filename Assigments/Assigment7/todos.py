# Author: Talha Gill


print("Welcome to your todo list")

todos = []
completed = []


while True:
    command = input("(V)iew, (A)dd, (R)emove, or (Q)uit: ").lower().strip()
    if command == "q":
        break
    elif command == "v":
        while True:
            command1 = input("View (T)odos or (C)ompleted Items? ").lower().strip()
            if command1 == "t":
                if len(todos) != 0:
                    for todo in todos:
                        print("-", todo)
                else:
                    print("You have no todos")
                break
            elif command1 == "c":
                if len(completed) != 0:
                    for complete in completed:
                        print("-", complete)
                else:
                    print("You have no done items")
                break
            else:
                print("Invalid input, try again.")
    elif command == "a":
        # ask the user for a todo 
        # if they entered something other than white space, append it to the list
        todo = input("Enter todo: ").strip()
        if (todo != "" and (todo in todos) == False):
            todos.append(todo)
        else:
            print("Sorry", todo, "is not in your list")
    elif command == "r":
        todo = input("Enter todo: ").strip()
        if todo in todos:
            todos.remove(todo) 
            completed.append(todo)
        else:
            print("Sorry", todo, "is not in your list")
    else:
        print("Invalid command")
   








print("GoodBye")
