
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
def find_average(numbers):
    sum = 0

    for number in numbers:
        sum += number

    print("Average is: ",sum / len(numbers))

find_average([1,2,3,4,5])