class Developer():
    def __init__(self, name, surName, number, salary, langs):
        self.name = name
        self.surName = surName
        self.number = number
        self.salary = salary
        self.langs = langs

    def showInfo(self):
        print("""
        Information About Developer:
        
        Name: {}
        
        Surname: {}
        
        Number: {}
        
        Salary: {}
        
        Languages: {}
        """.format(self.name, self.surName, self.number, self.salary, self.langs))

    def giveRaise(self, raise_amount:int):
        print("Raise is given!")
        self.salary += raise_amount

    def addLanguage(self, newLang):
        print("Language added!")
        self.langs.append(newLang)






dev = Developer("Kaan", "Bağrıyanık", 124325, 10000, ["Python", "Java", "C#"])

dev.showInfo()
dev.giveRaise(5000)
dev.showInfo()
dev.addLanguage("JavaScript")
dev.showInfo()