"""num = int(input("Enter a number to check: "))
divisors_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisors_sum += i

if divisors_sum == num:
    print("It's a perfect number!")
else:
    print("IT'S NOT!")

"""

"""num = input("Enter a number: ")
if len(num) == 3:
    if int(num[0])**3 + int(num[1])**3 + int(num[2])**3 == int(num):
        print("It's am Armstrong number!")
    else:
        print("No it's not!")
elif len(num) == 4:
    if int(num[0])**4 + int(num[1])**4 + int(num[2])**4 + int(num[3])**4 == int(num):
        print("It's an Armstrong number!")
    else:
        print("No it's not!")"""

"""for i in range(1, 10):
    for j in range(1, 10):
        print(j, " x ", i, " = ", i * j,sep="", end="            ")
    print()"""

"""sum = 0
while True:
    num = input("Enter number to sum: \nPress 1 to finish..")
    if num == "q":
        break
    sum += int(num)

print("Sum is: {}".format(sum))"""

"""for i in range(1, 101):
    if i % 3 != 0:
        continue
    else:
        print(i)
        
        """

list = [i for i in range(1,101) if i % 2 == 0]

print(list)

help(list.append)



"""num = input("Enter a number: ")
pow = len(num)
num = int(num)
sum = 0
numCont = num
while numCont > 0:
    sum += (numCont % 10)**pow
    numCont //= 10

if sum == num:
    print("It's an armstrong number!")
else:
    print("It's not!")
"""

