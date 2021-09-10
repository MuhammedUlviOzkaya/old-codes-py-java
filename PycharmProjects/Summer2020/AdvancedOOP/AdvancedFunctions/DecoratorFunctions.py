import time
def calculate_time(func):
    def wrapper(numbers):
        st = time.time()

        result = func(numbers)
        et = time.time()

        print(func.__name__ + " took " + str(et - st) + " seconds.")
        return result
    return wrapper




@calculate_time
def squares(numbers):
    result = list()

    for i in numbers:
        result.append(i ** 2)

    return result


def cubes(numbers):
    result = list()

    for i in numbers:
        result.append(i ** 3)

    return result

def extra(function):

    def wrapper(numbers):
        evens_sum = 0
        even_numbers = 0

        odds_sum = 0
        odd_numbers = 0

        for number in numbers:
            if number % 2 == 0:

                evens_sum += number
                even_numbers += 1
            else:

                odds_sum += number
                odd_numbers += 1

        print("Sum of evens is: ", evens_sum)
        print("Sum of odds is: ", odds_sum)

        function(numbers)

    return wrapper
@extra
def average(numbers):
    sum = 0
    for i in numbers:
        sum += i

    print(sum / len(numbers))



average([1,2,3,4,5])



















"""import time

def calculate_time(func):
    def wrapper(numbers):
        starting = time.time()

        result = func(numbers)

        ending = time.time()

        print(func.__name__ + " took " + str(ending - starting) + " seconds.")
        return result
    return wrapper

@calculate_time
def squares(numbers):
    result = list()

    for i in numbers:
        result.append(i ** 2)

    return result

@calculate_time
def cubes(numbers):
    result = list()

    for i in numbers:
        result.append(i ** 3)

    return result




def uppercase_decorator(function):

    def wrapper():

        return function().upper()

    return wrapper


def split_string(function):

    def wrapper():

        return function().split()

    return wrapper


@split_string
@uppercase_decorator
def hey():
    return "Hey There"

def decorator_with_arguments(function):

    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are {} and {}.".format(arg1, arg2))
        function(arg1, arg2)

    return wrapper_accepting_arguments




@decorator_with_arguments
def cities(city_one, city_two):

    print("Cities i love are {} and {}.".format(city_one, city_two))

cities("İstanbul", "İzmir")"""