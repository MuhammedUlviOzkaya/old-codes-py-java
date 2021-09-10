bookList = list()

menu = """
[1] - Add Book
[2] - Rent Book
[3] - List All
[Q] - Exit

"""
def addBook(book:tuple, list:list):
    list.append(book)
    print("Adding completed.. Press enter to return to main menu..")
    input()


def control(book:tuple, list:list):
    if book in list:
        return True
    else:
        return False

def rentBook(book:tuple, list:list):
    if control(book,list):
        list.remove(book)
        print("Renting completed.. Press enter to return to  main menu..")
        input()
    else:
        print("The book you're looking for is not available.. Press enter to return to main menu..")
        input()

def listThem(list:list):
    for i in list:
        print("Book Name: {}   ----->>>>>   Author: {}".format(i[0],i[1]))
    print("Listing completed.. Press enter to return to main menu..")
    input()




while True:
    print(menu)
    selection = input("Enter operation number: ")
    if selection == '1':
        bookName = input("Enter book name: ")
        authorName = input("Enter author name: ")
        book = (bookName, authorName)
        addBook(book, bookList)

    elif selection == '2':
        bookName = input("Enter book name: ")
        authorName = input("Enter author name: ")
        book = (bookName, authorName)
        rentBook(book,bookList)

    elif selection == '3':
        listThem(bookList)
    elif selection == 'q' or selection == 'Q':
        print("Have a nice one!")
        quit()
    else:
        print("Incorrect entrance!")

