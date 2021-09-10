first = 1
second = 1
index = 2

while len(str(second)) != 1000:
    temp = first + second
    first = second
    second = temp
    index += 1


print(index)

