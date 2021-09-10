class Computer():

    def __init__(self, name = "B U Z  S P R A Y S", processor = "AMD", ram = "4 GB", storage = "512 GB", fans = 2):
        self.name = name
        self.storage = storage
        self.ram = ram
        self.processor = processor
        self.fans = fans

    def __str__(self):
        return "Name: {}\nProcessor: {}\nRam: {}\nStorage: {}\nFans: {}".format(self.name, self.processor, self.ram, self.storage, self.fans)
