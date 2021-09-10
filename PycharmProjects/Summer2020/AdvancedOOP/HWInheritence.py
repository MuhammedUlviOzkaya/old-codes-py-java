class Animal():

    def __init__(self, color, eyes):
        self.color = color
        self.eyes = eyes

    def __str__(self):
        return "Color: {}\nEyes: {}".format(self.color, self.eyes)

    def sit(self):
        print("sitted.")

    def stand_up(self):
        print("standed up.")

class Dog(Animal):

    def __init__(self, color, eyes):
        super().__init__(color, eyes)
        self.legs = 4


    def come(self):
        print("came.")

    def bark(self):
        print("Woof wof!")

class Bird(Animal):

    def __init__(self, color, eyes, wings, feather):
        super().__init__(color, eyes)
        self.wings = wings
        self.feather = feather

    def fly(self):
        print("It flied!")

    def sing(self):
        print("Bird's singing!")

class Horse(Animal):

    def __init__(self, color, eyes, mane_color, type):
        super().__init__(color, eyes)
        self.mane_color = mane_color
        self.type = type

    def __str__(self):
        return "Color: {}\nEyes: {}\nMane Color: {}\nType: {}".format(self.color, self.eyes, self.mane_color, self.type)

    def run(self):
        print("It's running!")

    def stop(self):
        print("It stopped.")



kopek = Dog("Gray", "Brown")
hayvan = Animal("White", "Red")
kus = Bird("Brown", "Black", "White", "Soft")



hayvan.sit()
kopek.stand_up()

kus.fly()
kus.sing()

print("\n\n\n")

at = Horse("Black", "Purple", "Silver", "Pet Horse")

print(at)
at.run()
at.stop()






