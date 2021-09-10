"""def body(height, weight):
    return (weight / (float(height / 100) * float(height / 100)))

height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

x = body(height, weight)

if x < 18.5:
    print("Thin")
elif x < 25:
    print("Normal")
elif x < 30:
    print("Overweight")
else:
    print("Oha aq")"""

"""n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

print("Max one is: {}".format(max(n1, n2, n3)))"""

"""vize1 = int(input("Vize 1: "))
vize2 = int(input("Vize 2: "))
final = int(input("Final: "))

total = vize1 * 0.3 + vize2 * 0.3 + final * 0.4
print(total)

if total >= 90:
    print("AA")
elif total >= 85:
    print("BA")
elif total >= 80:
    print("BB")
else:
    print("Sen okuma la")"""

"""selection = input("Üçgen veya dikdörtgen? :")
if selection.lower() == "üçgen":
    n1 = int(input("First value: "))
    n2 = int(input("Second value: "))
    n3 = int(input("Third value: "))
    if n1 + n2 < n3 or n1 + n3 < n2 or n2 + n3 < n1 or abs(n1 - n2) > n3 or abs(n1 - n3) > n2 or abs(n2 - n3) > n1:
        print("Böle bi üçgen yok.")
    elif n1 == n2 == n3:
        print("Eşkenar üçgen.")
    elif (n1 == n2 and n1 != n3) or (n2 == n3 and n1 != n2) or (n1 == n3 and n1 != n2):
        print("İkizkenar üçgen.")
    elif n1 != n2 and n2 != n3 and n1 != n3:
        print("Çeşitkenar üçgen.")"""

"""i = 0

while i < 10:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
"""

"""print(*range(100))

print(*range(5, 100, 5))"""

"""list1 = [1, 2, 3, 4, 5]

list2 = []
for i in list1:
    list2.append(i)

print(list1)
print(list2)
"""

"""fibonacci = [1, 1]
for i in range(18):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)
print(len(fibonacci))

a = 5
b = 7

a,b = b,a #swaps
"""

a = 1
b = 1
fibonacci = [a, b]

for i in range(20):
    a,b = b, a+b
    fibonacci.append(b)

print(fibonacci)


