"""def hey(isim = "default"):
    print("Hey {}".format(isim))

hey("Ulvi")
print()

#SETTING DEFAULT VALUES
def info(name = "no info", surname = "no info", number = "no info"):
    print("Name: {}\nSurname: {}\nNumber: {}".format(name,surname,number))

info("Muhammed")
print(end="\n\n")

info(surname = "özkaya", number="17")

def sum(*x):
    sum = 0
    for i in x:
        sum += i
    return sum

def show(*name):
    for i in name:
        print(i)

show("Muhammed", "Ulvi", "Özkaya")

def func(*a):
    for i in a:
        print(i)

func("Muhammed", 17, )"""

a = 10      #global
def func():
    a = 4   #local
    print(a)
func()
print(a)

b = 20      #global
def fonk():
    global b
    b = 5   #global
    print(b)


fonk()
print(b)

