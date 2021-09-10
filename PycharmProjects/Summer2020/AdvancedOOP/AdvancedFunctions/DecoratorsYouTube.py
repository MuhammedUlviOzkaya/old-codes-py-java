def decoratorFunction(original_function):

    def wrapperFunction(*args, **kwargs):
        print("Wrapper things..")
        print(f"Original function before the '{original_function.__name__}'")

        return original_function(*args, **kwargs)

    return wrapperFunction


@decoratorFunction
def my_function():
    print("This is from my function.")

@decoratorFunction
def displayInfo(name, age):
    print(f"My name is {name} and i'm {age}")


displayInfo("Ulvi", 20)



