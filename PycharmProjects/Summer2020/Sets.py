string = "araba"

setA = set(string)

print(setA)

emptySet = {"banana", "apple", "watermelon",17 ,10}
print(type(emptySet))

emptySet.add(49)
emptySet.discard("apple")
print(emptySet)

x = set([1,2,3,4,5])
print(x)

y = set([2,4,6,8])
print(x.difference(y)) #kümeler fark işlemi

y.difference_update(x)

print(y)


# x.clear() empties the set

# set3 = x.union(y)   #returns a new set with all items from both sets

#print(set3)

x.update(y)  # inserts the items in y into x
print(x)

set4 = x.intersection(y)
print(set4)



