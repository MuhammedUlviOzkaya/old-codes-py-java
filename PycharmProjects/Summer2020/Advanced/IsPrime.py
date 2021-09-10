"""def isPrime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False
        return True

def perfectNum(num):
    sum = 0
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            sum += i
    if num == sum:
        return True
    else:
        return False

for i in range(1, 1000):
    if perfectNum(i):
        print(i)

"""
def ebob(num1, num2):
    minimum = min(num1, num2)
    maximum = max(num1, num2)
    ebob = 1
    for i in range(1, minimum + 1):
        if minimum % i == 0 and maximum % i == 0 and i > ebob:
            ebob = i

    print(ebob)



def ekok(num1, num2):
    minimum = min(num1, num2)
    maximum = max(num1, num2)
    for i in range(1, minimum + 1):
        if (i * maximum) % minimum == 0:
            return i * maximum


print(ekok(6, 7))



def okunus(num):
    if num / 10 >= 1:

        dict1 = {1 : "bir", 2 : "iki", 3 : "üç", 4 : "dört", 5 : "beş", 6 : "altı", 7 : "yedi", 8 : "sekiz", 9 : "dokuz", 0 : ""}
        dict2 = {1 : "on", 2 : "yirmi", 3 : "otuz", 4 : "kırk", 5 : "elli", 6 : "altmış", 7 : "yetmiş", 8 : "seksen", 9 : "doksan"}
        print(dict2[num // 10], dict1[num % 10])
    else:
        print("Lütfen 2 basamaklı bir sayı girin!")

def pisagor():
    for i in range(1, 101):
        for j in range(1, 101):
            c = (i**2 + j**2) ** 0.5
            if (c == int(c)):
                print("a:", i ,"b:", j, "c:", int(c))



