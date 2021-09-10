a = [1,1,1,2,3,4,5,4,6,4,43,5]

a = set(a)

print(a)

b = set("BUZ SPRAYS")

print(b)

c = {"buz", "sprays", "buz"}         #HOLDS 2 ELEMENTS BECAUSE SETS DON'T ALLOW DUPLICATION

print(c)

c.add("muhammed")
c.add("özkaya")

print(c)

x = {1,2,3,4,5}
y = {1,2}

dif = x.difference(y)

print(type(dif))

x.difference_update(y)        #UPDATES X

print(x)

x.discard(4)                  #DELETES ELEMENT FROM SET

print(x)

k1 = {1,3,5,7,9}
k2 = {1,5,9}

print(k1.intersection(k2))    #RETURNS COMMON ELEMENTS OF 2 SETS

k3 = {1,3,5,7}
k4 = {2,4,6,8}

print(k3.isdisjoint(k4))      #RETURNS TRUE IF SETS DON'T HAVE COMMON ELEMENT

print(k3.issubset(k1))        #SUBSET CONTROL

print(k3.union(k4))           #COMBINES SETS

