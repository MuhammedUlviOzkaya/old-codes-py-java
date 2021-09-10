
def amicable(num):
    sum = 0
    for j in range(1, num):
        divisorSum = 0
        divisorNum = 0
        for i in range(1, int(j / 2) + 1):
            if j % i == 0:
                divisorSum += i

        for k in range(1, int(divisorSum / 2) + 1):
            if divisorSum % k == 0:
                divisorNum += k

        if j == divisorNum and j != divisorSum:
            sum += j

    return sum




print(amicable(10000))