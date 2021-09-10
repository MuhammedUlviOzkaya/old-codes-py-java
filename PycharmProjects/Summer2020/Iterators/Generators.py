"""def squares():
    for i in range(1, 6):
        yield i ** 2

generator = squares()
print(generator)

iterator = iter(generator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))"""

def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            yield "{} x {} = {}".format(i, j, i * j)
        print()

for i in multiplication_table():
    print(i)

