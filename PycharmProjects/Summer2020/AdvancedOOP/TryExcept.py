"""try:
    a = int("325gfd4")
    print("Program is here")
except:
    print("There is an error!")

print("Blocks have ended")

"""

"""try:
    n1 = int(input("Num1: "))
    n2 = int(input("Num2: "))
    print(n1 / n2)
except ValueError:
    print("Please enter numbers correctly..")
except ZeroDivisionError:
    print("A number can't be divided by zero!")

print("Blocks have ended.")"""




"""try:
    n1 = int(input("Num1: "))
    n2 = int(input("Num2: "))
    print(n1 / n2)
except (ValueError, ZeroDivisionError):
    print("Value Error or Zero Division Error!")
finally:
    print("Finally block run.")
print("Blocks have ended.")"""


def reverse(s):
    if type(s) != str:
        raise ValueError("Please assing a string value..")
    else:
        print(s[::-1])

reverse(10)

