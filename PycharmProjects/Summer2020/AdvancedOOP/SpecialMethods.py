class Book():
    pass

book1 = Book()

print(book1)

del book1

class Book():

    def __init__(self, name, author, page, type):
        print("This is init function")
        self.name = name
        self.author = author
        self.page = page
        self.type = type

    def __str__(self):
        return "{}".format(self.name)

    def __len__(self):
        return self.page

    def __del__(self):
        print("{} is being deleted..".format(self.name))

kitap = Book("Yüce Aşk", "Motive", 432, "Love")

print(kitap)

print(len(kitap))
del kitap

print(kitap)