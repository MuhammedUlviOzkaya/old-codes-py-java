class Power3():
    def __init__(self, max = 0):

        self.max = max
        self.power = 0

    def __iter__(self):

        return self

    def __next__(self):
        if self.power <= self.max:
            result = 3 ** self.power

            self.power += 1

            return result

        else:
            self.power = 0
            raise StopIteration

power = Power3(6)

iterator = iter(power)

f"""or i in power:
    print(i)

for j in power:
    print(j)"""

def fibonacci():

    a = 1
    b = 1
    yield a
    yield b

    while True:
        a, b = b, a+b

        yield b

for num in fibonacci():

    if num > 100000:
        break
    print(num)