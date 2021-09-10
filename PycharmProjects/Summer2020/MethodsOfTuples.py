book1 = ("No.1", "Çiçeklerde Bir Telaş Var", 7000) #we use tuples bc they don't have to change and they are fast

print("Author               : {}".format(book1[0]))
print("Book Name            : {}".format(book1[1]))
print("Number of Pages      : {}".format(book1[2]))


library = []
library.append(book1)

print(library[0])
print("**********REMOVED**********")
library.remove(book1)
print(library)