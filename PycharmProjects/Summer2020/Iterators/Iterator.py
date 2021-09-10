"""list1 = [1,2,3,4,5]

iterator = iter(list1)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break"""

class Remote():
    def __init__(self, channel_list):
        self.channel_list = channel_list
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.channel_list):
            return self.channel_list[self.index]
        else:
            self.index = -1
            raise StopIteration

controller = Remote(["atv", "kanal d", "bein sports", "star tv"])

iterator = iter(controller)

for i in controller:
    print(i)
