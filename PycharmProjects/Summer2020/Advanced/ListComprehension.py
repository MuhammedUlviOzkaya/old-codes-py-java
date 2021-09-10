"""list = [1, 2, 3, 4, 5]
list2 = [i for i in list]

print(list2)

list3 = [i*i for i in list2]
print(list3)


list4 = [(1,2), (3,4), (5,6)]
list5 = [i * j for i, j in list4]
print(list5)

s = "Buz Sprays"
list_buz = [i * 3 for i in s]
print(list_buz)
"""

"""list = [[1, 2, 3], [45, 6], [7, 8]]
for i in list:
    for x in i:
        print(x)
"""
list2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
list3 = [j for i in list2 for j in i]
print(list3)


s = "Şamil"

