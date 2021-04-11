FILE_NAME = "book.txt"

#write an array of books to the fike books.txt
def write_books(books):
    with open(FILE_NAME, "w") as file:
        for book in books:
            file.write(book +"\n")
#read in the each line from the fike books.txt and array of books
def read_books():
    books = []
    with open(FILE_NAME) as file:
        for line in file:
            line = line.replace("\n","").strip()
            books.append(line)
    return books

# displat a list of books, to the console, in formation 1. bookName
def list_books(books):
    for i in range(len(books)):
        print(f"{i+1}.  {books[i]}")

# add a book to the list of books to the file
def add_book(books):
    book = input("Book: ").strip()
    books.append(book)
    write_books(books)
    print(f"{book} was added.")
    return books

#remove a book from the list of books
def delete_book():
    index = int(input("Enter book name: "))

    # if the book is not in the valid range
    if index < 0 or index >= len(books):
        print(f"Sorry, valid numbers are between 1 and {lens(books)}")
    else:
        book = books.pop(index)
        write_books(books)
        print(f"{book} was deleted")

while True:
    command = input("Enter (L):ist, (A)dd, (D)elete, or (Q)uit.") .lower() .strip()
    books = read_books()
    if command == "l":
        list_books(books)
    elif command == "a":
        books = add_book(books)
    elif command == "d":
        books = delete_book(books)
    elif command == "q":
        break
    else:
        print("Invalid command, try again.")

print("Goodbye")
