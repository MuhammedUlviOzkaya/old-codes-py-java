class Worker():

    def __init__(self, name = "none", salary = "none", department = "none"):
        print("This is init func of worker class")

        self.name = name
        self.salary = salary
        self.department = department

    def showInfo(self):
        print("Information abour worker class..")

        print("Name: {}\nSalary: {}\nDepartment: {}".format(self.name, self.salary, self.department))

    def change_department(self, new_department):
        print("Department changed!")
        self.department = new_department

class Manager(Worker):
    def give_raise(self, raise_amount: int):
        self.salary += raise_amount
        print("Raise is given!")

man = Manager("Kaan Bağrıyanık", 7500, "Software")
man.showInfo()

man.change_department("Hardware")
man.showInfo()

man.give_raise(1000)

man2 = Manager("Muhammed Ulvi Özkaya", 7500, "Software")

man2.showInfo()

man2.give_raise(500)

man2.showInfo()