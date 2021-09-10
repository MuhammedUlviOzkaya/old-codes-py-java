from LibraryProject import *

print("""**************************************

Welcome To Library Program

[1] - Show Books
[2] - Find Book
[3] - Add Book
[4] - Delete Book
[5] - Update Edition

Press \"q\" to exit..

**************************************

""")

library = Library()




while True:
    selection = input("Your selection: ")

    if selection == "q":
        print("Exitted.")
        exit()

    elif selection == "1":
        library.show_books()

    elif selection == "2":
        name = input("Name of book you're finding: ")
        library.book_query(name)

    elif selection == "3":
        name = input("Name: ")
        author = input("Author: ")
        publisher = input("Publisher: ")
        genre = input("Genre: ")
        edition = input("Edition: ")

        new_book = Book(name, author, publisher, genre, edition)

        library.add_book(new_book)
        print("Book is added!")

    elif selection == "4":
        name = input("Name of book you want to delete: ")

        answer = input("Are you sure? (Y/N)")
        if answer == "Y":
            library.delete_book(name)
            print("Book is deleted!")
        else:
            continue

    elif selection == "5":
        name = input("Name of book you want to update edition: ")
        library.edition_up()
        print("Edition is updated!")

    else:
        print("Incorrect Entrance..")



