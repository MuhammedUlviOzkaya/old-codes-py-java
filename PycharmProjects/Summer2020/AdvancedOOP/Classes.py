class Car():
    model = "Mercedes AMG"
    color = "Gray"
    horsePower = 170
    def __init__(self, model, color, horsePower):
        print("Print function is called")
        self.model = model
        self.color = color
        self.horsePower = horsePower

myCar = Car("Merco", "Gray", 190)

class Araba():
    def __init__(self, model = "none", color = "none", horsePower = 0):
        self.model = model
        self.color = color
        self.horsePower = horsePower

yeniAraba = Araba()
enYeniAraba = Araba(color="red", horsePower=130)

print(enYeniAraba.model)
print(enYeniAraba.color)
print(enYeniAraba.horsePower)







