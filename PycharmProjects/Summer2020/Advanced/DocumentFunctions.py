try:
    file = open("C:/Users/buzon/Desktop/bilgiler.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Document Not Found")

"""with open("C:/Users/buzon/Desktop/bilgiler.txt", "r", encoding="utf-8") as file:
    for i in file:
        print(i)
"""

"""with open("C:/Users/buzon/Desktop/bilgiler.txt", "r", encoding="utf-8") as file:
    print(file.tell())
    file.seek(20)
    print(file.tell())"""

with open("C:/Users/buzon/Desktop/bilgiler.txt", "r", encoding="utf-8") as file:

    content = file.read()

    print(content)
    print(file.tell()) #tells cursor's place
    file.seek(0) #changes cursor's place
    print()
    content2 = file.read(14)
    print(content2)