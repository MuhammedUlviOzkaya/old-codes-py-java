bookList = list()

menu = """
[1] - Add Book
[2] - Delete Book
[3] - List Books
[Q] - Exit
"""

def addBook(book, list):
    list += [book]
    print("Book added!")
    input("Press enter to return main menu")

def deleteBook():
    pass

def listBooks(list):
    for i in list:
        print("Book Name   ------>>>>>>   {}".format(i))
    input("Press enter to return main menu")

def exit():
    quit()

while True:
    print(menu)
    selection = input("Type action number..")
    if selection == '1':
        bookName = input("Enter book name: ")
        addBook(bookName, bookList)
    elif selection == '2':
         deleteBook()
    elif selection == '3':
        listBooks(bookList)
    elif selection == 'q' or selection == 'Q':
        exit()
    else:
        print("Invalid code")
        input("Press enter to return main menu")