dict1 = {1 : "one", 2 : "two", 3 : "three", 4 : 4}

x = dict1.items()

print(x)

"""for i in dict1.items():
    print(i)"""

for i, j in dict1.items():
    print(i, j)