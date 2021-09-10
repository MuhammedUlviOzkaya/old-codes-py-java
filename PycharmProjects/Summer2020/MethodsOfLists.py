myList = [1,2,3,4]
myList2 = myList


print(myList.count(1))

myList.append("Buz")
myList.remove(3)

print(myList, myList, sep="\n") # both print the same result bc our list has not copied

print("="*25)
print(myList)
print("Operations")
myNewList = myList.copy()

myList.append(10)
myList.remove(4)
print(myList)
print(myNewList)

myList.extend(myNewList) #puts them together
print(myList)

index = myList.index(4)
print(index)

listt = [1,5,78,4,8,6]
print(listt)
listt.sort()
print(listt)

print(listt[2:]) # prints from 2nd index
