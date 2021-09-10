divided = float(input("Divided: "))
dividing = float(input("Dividing: "))

try:
    print("Result is: ", divided / dividing)
except ZeroDivisionError as error:
    print("You can not divide a number with 0")
    print("Real error is: ")
    print(error)
except TypeError as error2:
    print("There is a type error and :")
    print(error2)

except:                     #It catches every errors.
    print("Error or errors found.")

finally:
    print("You always see this message at the end of operations or errors.")

