def sumOfDigits(num:float):
    sum = 0
    num = str(num)
    for i in range(len(num)):
        sum += int(num[i])
    return sum

def sumOfTwos():
    a = (1 - 2**1001) / (1 - 2)
    return a

print(sumOfTwos())


