"""pay = 0

hour = int(input("Enter hour: "))

if hour == 1:
    pay = 10
elif hour >= 2 and hour <=5:
    pay = 10 + 3 * (hour - 1)
else:
    pay = 22 + 4 * (hour - 5)

print(pay)"""


names = []

entrance = input("Enter names seperated with commas: ")

nameList = entrance.split(",")

for i in nameList:
    names.append(i.strip())


names.sort()
print(names)

