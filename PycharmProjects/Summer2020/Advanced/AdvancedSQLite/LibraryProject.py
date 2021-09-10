import sqlite3
import time

class Book():

    def __init__(self, name, author, publisher, genre, edition):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.edition = edition

    def __str__(self):
        return "Name: {}\nAuthor: {}\nPublisher: {}\nGenre: {}\nEdition: {}".format(self.name,self.author,self.publisher,self.genre,self.edition)


class Library():

    def __init__(self):

        self.connect()

    def connect(self):

        self.connection = sqlite3.connect("library.db")

        self.cursor = self.connection.cursor()

        query = "create table if not exists books (BookName TEXT, Author TEXT, Publisher TEXT, Genre TEXT, Edition INT)"

        self.cursor.execute(query)

        self.connection.commit()

    def disconnect(self):

        self.connection.close()

    def show_books(self):

        query = "select * from books"

        self.cursor.execute(query)

        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There is no book in library.")
        else:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)

    def book_query(self, name):

        query = "select * from books where BookName = ?"

        self.cursor.execute(query, (name,))

        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There is no such book.")
        else:
            book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])

            print(book)

    def add_book(self, book):

        query = "insert into books values(?,?,?,?,?)"

        self.cursor.execute(query, (book.name, book.author, book.publisher, book.genre, book.edition))

        self.connection.commit()

    def delete_book(self, name):

        query = "delete from books where BookName = ?"

        self.cursor.execute(query, (name,))

        self.connection.commit()

    def edition_up(self, name):

        query = "select * from books where BookName = ?"

        self.cursor.execute(query, (name,))

        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There is no such book.")
        else:
            edition = books[0][4]

            edition += 1

            query2 = "update books set Edition = ? where BookName = ?"

            self.cursor.execute(query2, (edition, name))

            self.connection.commit()

