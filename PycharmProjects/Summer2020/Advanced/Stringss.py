s = "buz"

print(s.startswith("b"))      #RETURNS TRUE

print(s.endswith("z"))        #RETURNS TRUE

a = "                           buz                          "

print(a)
print(a.strip())

print(a.lstrip())

print(a.rstrip())

b = "---------------------------------buz--------------------------------"

print(b)

print(b.strip("-"))

list = ["21", "09", "1999"]

print(".".join(list))

list2 = ["T", "B", "M", "M"]

print(".".join(list2))

s1 = "Galatasaray"
print(s1.count("a"))

print(s1.count("a", 3))     #RETURNS NUMBER OF "A" FROM THE INDEX SENT

print("buzum".count("u"))

print("buzum".find("a"))    #RETURNS -1 IF IT DOESN'T CONTAIN

print("buzum".find("u"))      #RETURNS THE INDEX OF FINDING PART

print("buzum".find("u", "buzum".find("u") + 1))        #RETURNS THE INDEX OF SECOND "U"


