import os
#doc = open("text.txt", "w")                   # it's used for writing. If it exists, it deletes and rewrite.

#doc.write("Muhammed Ulvi Özkaya\n")
#doc.write("Buz Sprays\n")
#doc.write("Lorenzo is my former name")

#doc.close()

#doc = open("text.txt", "r")                   #it's used for reading.

#print(doc.read())

# doc = open("text.txt", "a")                 #it's used for writing. It doesn't delete if it's exist. It adds.
# doc = open("text.txt", "x")                 #it's used for writing. If ıt exists, it runs an error.

doc = open("test.txt", "r+")
print(doc.read())
doc.write("Old datas has deleted and this is the new one!")

doc.close()

if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("Deleted!")
else:
    print("The file does not exist!")
















