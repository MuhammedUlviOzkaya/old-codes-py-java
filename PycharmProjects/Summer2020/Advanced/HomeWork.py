"""s = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

print(s.count("m"))"""

"""with open("odev.txt", "r", encoding = "utf-8") as file:
    content = file.read()


content = content.split("\n")

print(content)
word = list()
for i in range(len(content)):
    content[i] = content[i].replace(" ", "")
    word.append(content[i][0])

for i in word:
    print(i, end="")"""

"""with open("mails.txt", "r", encoding = "utf-8") as file:
    content = file.read()

content = content.split("\n")
print(content)

mails = list()

for i in content:
    if i.endswith(".com") and i.find("@") != -1:
        mails.append(i)

print(mails)"""

names = ["Kerim","Tarık","Ezgi","Kemal","Ilkay","Sükran","Merve"]
sur_names = ["Yılmaz","Oztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

full = list()

for i in range(len(names)):
    fullName = names[i] + " " + sur_names[i]
    full.append(fullName)

full.sort()
print(full)









