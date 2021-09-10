s = "Ulvi"
if "l" in s:
    print("It contains l")
else:
    print("It doesn't contain l")


s2 = "Buz Sprays"
if "uz" not in s2:
    print("Not in s2")
else:
    print("Buz Sprays contains uz")

giris = input("Enter mail")
if "@" not in giris:
    print("You must use '@' to enter your mail adress.")
else:
    print("Mail adress updated!")