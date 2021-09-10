with open("C:/Users/buzon/Desktop/bilgiler.txt", "r+", encoding="utf-8") as file:
    print(file.read())


"""with open("C:/Users/buzon/Desktop/bilgiler.txt", "r+", encoding="utf-8") as file:
    file.seek(10)
    file.write("Muhammed")

with open("C:/Users/buzon/Desktop/bilgiler.txt", "r+", encoding="utf-8") as file:
    print(file.read())"""


"""with open("C:/Users/buzon/Desktop/bilgiler.txt", "a", encoding="utf-8") as file:
    file.write("buzonekk\n")

with open("C:/Users/buzon/Desktop/bilgiler.txt", "r", encoding="utf-8") as file:
    print(file.read())"""

"""with open("C:/Users/buzon/Desktop/bilgiler.txt", "r+", encoding="utf-8") as file:
    content = file.read()
    content = "Muhammed Ulvi Özkaya\n" + content
    file.seek(0)
    file.write(content)"""

"""with open("C:/Users/buzon/Desktop/bilgiler.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    print(list)
    list.insert(2, "MSI Notebook\n")
    print(list)
    file.seek(0)
    for i in list:
        file.write(i)
    print(file.read())
"""
