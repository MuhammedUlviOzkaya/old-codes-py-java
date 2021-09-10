def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
sum = 0
a = str(factorial(100))
for i in range(len(a)):
    sum += int(a[i])
print(sum)