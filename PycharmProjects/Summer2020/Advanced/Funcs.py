# MAP FUNCTION
"""def double(n):
    return n * 2

a = list(map(double, [1,2,3,4,5,6]))

print(a)

b = list(map(lambda x : x ** 2, (1,2,3,4,5,6)))

print(b)


list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = [9,10,11,12,13]

c = list(map(lambda x,y : x * y, list1, list3))

print(c)"""

# REDUCE FUNCTION

"""from functools import reduce

def sum(x,y):
    return x + y

print(reduce(sum, [12,18,20,10]))

print(reduce(lambda x,y : x * y, [1,2,3,4,5]))

def maks(x, y):
    if x > y:
        return x
    else:
        return y

print(reduce(maks, [5,2,5,3,4]))
"""

"""def sum(x, y):
    return x + y

a = map(sum, ("apple", "banana", "melon"), ("orange", "lemon", "pineapple"))

print(list(a))"""

# REDUCE FUNCTION

"""from functools import reduce

list = [1,2,3,4,5]

list2 = [6,7,8,9]

def mult(x, y):
    return x * y

fact = reduce(mult, (5, 6))
print(fact)
"""

# FILTER FUNCTION


"""a = filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8])

print(list(a))

liste = [12,5,-64,-674,-65,356,46,3,6,5,-57,-67]

b = filter(lambda x : x < 0, liste)

print(list(b))

def isPositive(n):
    if n > 0:
        return True
    else:
        return False

c = filter(isPositive, liste)

print(list(c))"""

# ZIP FUNCTION


"""i = 0
result = list()
while i < len(list1) and i < len(list2):
    result.append((list1[i], list2[i]))
    i += 1

print(result)"""


"""list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10,11]


a = list(zip(list1, list2))

print(a)

list3 = ["Java", "Python", "Javascript", "HTML"]

b = list(zip(list1, list2, list3))

print(b)

for i, j in zip(list1, list3):
    print(i, j)

dict1 = {"Apple" : 0, "Pear" : 1, "Pineapple" : 2}
dict2 = {1 : "One", 2 : "Two", 3 : "Three", 4 : "Four"}

ls = list(zip(dict1, dict2))
lst = list(zip(dict1.values(), dict2.values()))
print(ls)

print(lst)
"""

# ENUMERATE
"""
liste = ["Java", "Python", "Javascript", "HTML"]

print(list(enumerate(liste)))

list = [0,1,2,3,4,5,6,7,8,9,10]

for i,j in enumerate(list):
    if i % 2 == 0:
        print(j)


"""






