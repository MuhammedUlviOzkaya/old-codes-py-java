"""def mult(liste):
    return liste[0] * liste[1]

liste = [(3,4),(10,3),(5,6),(1,9)]

print(list(map(mult, liste)))"""


"""def isTriangle(a):
    if (abs(a[0] + a[1]) > a[2] and abs(a[0] + a[2]) > a[1] and abs(a[1] + a[2]) > a[0]):
        return True
    else:
        return False

liste =  [(3, 4, 5), (6, 8, 10)]
print(list(filter(isTriangle, liste)))
"""
"""from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]

a = list(filter(lambda x : x % 2 == 0, liste))
print(reduce(lambda x, y : x + y, a))"""

names = ["Kerim","Tarık","Ezgi","Kemal","İlay","Şükran","Merve"]

surNames = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = list(zip(names, surNames))
for i, j in liste:
    print(i, j)





