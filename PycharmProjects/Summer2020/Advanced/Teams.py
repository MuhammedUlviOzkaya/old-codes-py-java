with open("players.txt", "r", encoding="utf-8") as file:
    list = file.read()

list = list.split("\n")
list.pop()
for i in range(len(list)):
    list[i] = list[i].split(",")

gs = []
fb = []
bjk = []


for i in list:
    if i[1] == "Galatasaray":
        gs.append(i)
    elif i[1] == "Fenerbahçe":
        fb.append(i)
    else:
        bjk.append(i)


with open("gs.txt", "w", encoding="utf-8") as dosya:
    for element in gs:
        dosya.write(element[0])
        dosya.write("\n")
with open("fb.txt", "w", encoding="utf-8") as dosya:
    for element in fb:
        dosya.write(element[0])
        dosya.write("\n")
with open("bjk.txt", "w", encoding="utf-8") as dosya:
    for element in bjk:
        dosya.write(element[0])
        dosya.write("\n")