import time
st = time.time()
def is_abundant(n):
    sum = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            sum += i

    if sum > n:
        return True
    else:
        return False

# if sum = num --> PERFECT
# if sum > num --> ABUNDANT
# if sum < num --> DEFICIENT

numbers = list(range(1, 28124))

abundants = list()
for i in range(12, 28124 - 12):
    if is_abundant(i):
        for a in abundants:
            if (a + i) in numbers:
                numbers.remove(a + i)
        abundants.append(i)

sum = 0
for i in numbers:
    sum += i

print(sum)




ft = time.time()

print(ft - st)


