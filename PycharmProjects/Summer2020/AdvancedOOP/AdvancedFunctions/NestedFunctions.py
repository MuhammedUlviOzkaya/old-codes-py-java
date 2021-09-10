def func(*args):
    for i in args:
        print(i)



def func2(name, *args):
    print("Name:", name)
    for i in args:
        print(i)

def func2(**kwargs):
    print(kwargs)

def func3(**kwargs):
    for i, j in kwargs.items():
        print("Argument Name:",i,"Argument Value:", j)

"""def func4(*args, **kwargs):
    for i in args:
        print(i)

    print("---------------------")

    for i, j in kwargs.items():
        print(i, j)

func4(1,2,34,5,4,4, name = "Buz", surName = "Sprays", number = 17)"""


"""def funct():
    print("Hey!")


hey = funct

hey()

del funct

hey()"""

"""def bigFunc():

    def smallFunc():
        print("This is from small function.")
    smallFunc()
    print("This is from big function.")

def fonk1(*args):

    def fonk2(args):
        sum = 0
        for i in args:
            sum += i
        return sum
    print(fonk2(args))

def mainFunc(operation_name):

    def sumOperation(*args):
        sum = 0
        for i in args:
            sum += i
        return sum

    def multiply(*args):
        mult = 1
        for i in args:
            mult *= i
        return mult

    if operation_name == "sum":
        return sumOperation
    else:
        return multiply

sumFunc = mainFunc("sum")

multFunc = mainFunc("multiply")"""

def sum(a,b):
    return a + b
def subtr(a,b):
    return a - b
def divide(a,b):
    return a / b
def multiply(a,b):
    return a * b

def mainFunction(sum, subtr, divide, multiply, operation_name):
    if operation_name == "sum":
        print(sum(6,8))
    elif operation_name == "subtr":
        print(subtr(98,27))
    elif operation_name == "divide":
        print(divide(64,4))
    elif operation_name == "multiply":
        print(multiply(6,7))

mainFunction(sum, subtr, divide, multiply, "subtr")













