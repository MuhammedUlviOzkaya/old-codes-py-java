"""sys_user_buz = "buzonekk"
sys_password = "321123"

counter = 3
while True:
    user = input("Enter username: ")
    password = input("Enter password: ")
    if user == sys_user_buz and password == sys_password:
        print("Entrance completed!")
        break
    else:
        print("Error!")
        counter -= 1

    if counter == 0:
        print("Exitted..")
        break
"""

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(35))