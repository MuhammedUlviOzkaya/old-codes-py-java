try:
    file = open("C:/Users/buzon/Desktop/bilgiler.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Document Not Found")

"""for i in file:
    print(i)"""

"""content = file.read().split("\n")
print(content)"""

"""print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
"""

list = file.readlines()
print(list)




