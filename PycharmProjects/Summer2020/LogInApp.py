users = {"Muhammed Ulvi Özkaya" : "buzonebuz",
         "Kaan Bağrıyanık" : "cimbombom"}


names = users.keys()

userName = input("Enter Username: ")
if userName in names:
    print("Welcome {}".format(userName))
    password = input("Enter Password: ")
    if password == users[userName]:
        print("You're In!")
    else:
        print("Incorrect Password!")
else:
    print("No user matched!")

