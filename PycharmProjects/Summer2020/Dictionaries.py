dictionary = dict()

dictionary1 = {"home" : "ev",
               "book" : "kitap",
               "art" : "sanat"}

print(dictionary1)
print(dictionary1["art"])
print(dictionary1["book"])

character1 = {"name" : "Sova",
              "power" : 186,
              "color" : "blue",
             "age" : 26}

print("Karakterin adı   : {}\nKarakterin rengi : {}".format(character1["name"],character1["color"]))
print("Karakterin gücü  : {}".format(character1["power"]))

character1["name"] = "Reyna"


print(character1["name"])

character2 = {"name" : "Breach",
              "power" : 197,
              "color" : "orange",
              "age" : 34}


def vur(vuran: dict, vurulan: dict):
    vurulan["power"] -= int(vuran["power"])

vur(character1, character2)

print(character2["power"])


