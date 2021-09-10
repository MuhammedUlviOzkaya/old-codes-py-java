func = lambda a, b, hypo : a**2 + b**2 == hypo**2


print(func(3,4,6))
print(func(3,4,5))

func1 = lambda x : x**2
print(func1(6))

fnc = lambda x, y : float((x + y) / 2)
print(fnc(4, 9))


def fonk(num):
    return lambda a : a * num

dbl = fonk(2)
print(dbl(10))






