class Soldier():
    weight = 70
    height = 175

    def __init__(self, name, power):
        self.weapon = 'Deagle'
        self.name = name
        self.power = power
        self.abilities = ["fighting"]

buz = Soldier("Muhammed", 109)

buz.abilities += ["running"]
buz.abilities += ["hunting"]
print(buz.abilities)

input("Press enter to return")
