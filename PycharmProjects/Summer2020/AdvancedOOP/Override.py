class Worker():
    def __init__(self, name, salary, department):
        print("This is init func of worker class..")
        self.name = name
        self.salary = salary
        self.department = department

    def change_departmet(self, new_department):
        self.department = new_department
        print("Department is changed!")

    def show_info(self):
        print("\nInformation about worker class: \nName: {}\nSalary: {}\nDepartment: {}".format(self.name, self.salary, self.department))

class Manager(Worker):
    def __init__(self, name, salary, department, people):
        print("This is init func of manager class..")
        super().__init__(name, salary, department)
        self.people = people


    def give_raise(self, raise_amount):
        self.salary += raise_amount
        print("Raise is given!")

    def show_info(self):
        print("\nInformation about manager class: \nName: {}\nSalary: {}\nDepartment: {}\nPeople: {}".format(self.name, self.salary, self.department, self.people))

yonetici = Manager("Hurşit Özkaya", 20000, "Hardware", 200)
print()
worky = Worker("Buz", 10000, "Freeee")

worky.show_info()

yonetici.show_info()
