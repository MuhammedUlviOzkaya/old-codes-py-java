"""
for num in range(1, 101):
    print("Bu ",num,"'ıncı sayı.",sep="")

for num1 in range(101):
    print()
"""
""" THEY ARE SAME """

for x in range(0, 61, 3):
    if x % 6 == 0:
        pass
    print(x)
"""3ER 3ER ARTAR"""

""" ELSE IN FOR LOOPS """
for y in range(6):
    print(y)
else:
    print("Loop is finished")
""" IT PRINTS WHEN THE LOOP ENDS """

""""NESTED LOOPS"""
adj = ["red", "big", "delicious"]
fruits = ["apple", "banana", "cherry"]

for ad in adj:
    for fru in fruits:
        print(ad, fru)