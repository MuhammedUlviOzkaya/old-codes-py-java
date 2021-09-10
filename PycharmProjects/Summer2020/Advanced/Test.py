"""import time
st = time.time()
list = [2]
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True

    for i in list:
        if n % i == 0:
            return False

    list.append(n)
    return True


sum = 0

for i in range(2, 100000):
    if isPrime(i):
        sum += i


print(sum)
ft = time.time()
print(ft-st)
print(len(list))

"""

"""fibonacci = [1,1]
sum = 0
while fibonacci[-1] <= 4000000:
    x = int(fibonacci[-1]) + int(fibonacci[-2])
    fibonacci.append(x)
    if x % 2 == 0:
        sum += x

print(sum)"""

"""list = [12,5,6,4,47,4,2,6]

print(all(list))
list2 = (True, True, True, False)


print(all(list2))
print(any(list2))"""

"""a = "buz one dir onun adı"

a = a.replace(" ", "")

print(a)
"""

liste = [0,1,2]

liste.remove(1)
liste.remove(3)
print(liste)






