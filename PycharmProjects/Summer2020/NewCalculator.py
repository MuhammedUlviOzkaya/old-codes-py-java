print("""
[1] - Addition
[2] - Subtraction
[3] - Multiplication
[4] - Division
[Q] - Exit
""")
data = input("Type: ")

if data == "1":
    x = input("First num:")
    x = float(x)
    y = input("Second num:")
    y = float(y)
    print("Answer is: ", x+y)
elif data == "2":
    x = input("First num:")
    x = float(x)
    y = input("Second num:")
    y = float(y)
    print("Answer is: ", x - y)
elif data == "3":
    x = input("First num:")
    x = float(x)
    y = input("Second num:")
    y = float(y)
    print("Answer is: ", x * y)
elif data == "4":
    x = input("First num:")
    x = float(x)
    y = input("Second num:")
    y = float(y)
    print("Answer is: ", x / y)
elif data == "q" or data == "Q":
    print("Quitted")
    quit()



