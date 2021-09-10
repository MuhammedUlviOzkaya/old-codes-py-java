class User():
    def __init__(self, name, customerNumber,password):
        self.name = name
        self.customerNumber = customerNumber
        self.password = password
        self.accounts = list()










class Account():
    def __init__(self, user:User, balance:int, minBalance:int, iban):
        self.user = user
        self.balance = balance
        self.minBalance = minBalance
        self.iban = iban



class main():
    allAccounts = list()
    users = list()


    while True:
        print("""
        [1] - I'm A Customer
        [2] - I Want To Be A Customer
        [Q] - Exit        
        """)
        selection = input("Enter your selection..")
        if selection == '1':
            customerNumber = input("Customer Number: ")
            for customer in users:
                if customerNumber == customer.customerNumber:
                    custPassword = input("Password: ")
                    if custPassword == customer.password:
                        print("WELCOME {}!".format(customer.name))
                        while True:
                            print("""
                            [1] - Show Accounts
                            [2] - Create An Account
                            [3] - Delete Account
                            [Q] - Exit
                            """)
                            selection2 = input("Enter your selection..")
                            if selection2 == '1':
                                if len(customer.accounts) == 0:
                                    print("You don't have an account yet..")
                                    input("Press Enter To Return..")
                                else:

                                    for accs in customer.accounts:
                                        print((customer.accounts.index(accs) + 1), ". Account =>\nBalance: {}\nMin Balance Limit: {}\nIBAN: {}".format(accs.balance, accs.minBalance, accs.iban),sep="")
                                        print(end="\n\n")
                                    chosen = input("Choose an account or return(r): ")
                                    if chosen == 'r' or chosen == 'R':
                                        pass
                                    elif chosen.isdigit():
                                        if int(chosen) <= len(customer.accounts):

                                            chosen = int(chosen)
                                            while True:
                                                print("""
                                                [1] - Deposit Money
                                                [2] - Withdraw Money
                                                [3] - Send Money
                                                [Q] - Exit
                                                
                                                """)
                                                operation = input("Choose An Operation..")
                                                if operation == '1':
                                                    depositAmount = input("Enter Amount To Deposit: ")
                                                    if depositAmount.isdigit():
                                                        depositAmount = int(depositAmount)
                                                        customer.accounts[chosen - 1].balance = int(customer.accounts[chosen - 1].balance)
                                                        customer.accounts[chosen - 1].balance += depositAmount
                                                        print("Operation Completed!\nNew Balance Is: {}".format(customer.accounts[chosen - 1].balance))
                                                        input("Press Enter To Return..")
                                                    else:
                                                        print("Amount Must Be Consist Of Numbers!\nPress Enter To Return..")
                                                        input()

                                                elif operation == '2':
                                                    withdrawAmount = int(input("Enter Amount To Withdraw: "))
                                                    if withdrawAmount <= customer.accounts[chosen - 1].balance:
                                                        customer.accounts[chosen - 1].balance -= withdrawAmount
                                                        print("Operation Completed!\nNew Balance Is: {}".format(customer.accounts[chosen - 1].balance))
                                                        input("Press Enter To Return")
                                                    else:
                                                        print("Insufficient Balance!\nPress Enter To Return")
                                                        input()
                                                elif operation == '3':
                                                    receiverIban = input("Receiver Account's IBAN: ")
                                                    for i in range(len(users)):
                                                        for accos in users[i].accounts:
                                                            if accos.iban == receiverIban:
                                                                print(accos.user.name)
                                                                sendAmount = int(input("Enter Amount You Want To Send: "))
                                                                if customer.accounts[chosen - 1].balance >= sendAmount:
                                                                    customer.accounts[chosen - 1].balance -= sendAmount
                                                                    accos.balance += sendAmount
                                                                    print("Operation Completed!\nNew Balance Is: {}".format(customer.accounts[chosen - 1].balance))
                                                                    input("Press Enter To Return..")



                                                                else:
                                                                    print("Insufficient Balance!")
                                                                    input("Press Enter To Return..")
                                                            else:
                                                                print("Customer Couldn't Found!\nPress Enter To Return..")
                                                                input()
                                                elif operation == 'Q' or operation == 'q':
                                                    break
                                                else:
                                                    print("Incorrect Entrance!\nPress Enter To Return..")
                                                    input()
                                        else:
                                            print("Incorrect Entance!\nPress Enter To Return..")
                                            input()
                                    else:
                                        print("Incorrect Entrance!\nPress Enter To Return..")
                                        input()

                            elif selection2 == '2':
                                if len(customer.accounts) < 5:
                                    balance = input("Balance: ")
                                    if balance.isdigit():

                                        balance = int(balance)
                                        minBalance = int(input("Min Balance Limit: "))
                                        iban = input("Enter An Identifier (Like IBAN): ")
                                        customer.accounts.append(Account(customer, balance, minBalance, iban))
                                        allAccounts.append(Account(customer, balance, minBalance, iban))
                                        print("New Account Created!\nPress Enter To Return To Main Menu..")
                                        input()
                                    else:
                                        print("Incorrect Entrance!\nPress Enter To Return..")
                                        input()

                                else:
                                    print("You can have max 5 accounts!")
                                    input("Press Enter To Return..")
                            elif selection2 == '3':
                                if len(customer.accounts) < 2:
                                    print("You Can't Delete Account When You Have Only 1!\nPress Enter To Return..")
                                    input()
                                else:
                                    for accs in customer.accounts:
                                        print((customer.accounts.index(accs) + 1),
                                              ". Account =>\nBalance: {}\nMin Balance Limit: {}\nIBAN: {}".format(accs.balance, accs.minBalance, accs.iban), sep="")
                                        print(end="\n\n")
                                    delSelect = input("Choose Account You Want To Delete: ")
                                    if delSelect.isdigit():
                                        if int(delSelect) <= len(customer.accounts):

                                            for accs in customer.accounts:
                                                if (customer.accounts.index(accs) + 1) == delSelect:
                                                    pass
                                                else:
                                                    print((customer.accounts.index(accs) + 1),
                                                          ". Account =>\nBalance: {}\nMin Balance Limit: {}\nIBAN: {}".format(accs.balance, accs.minBalance, accs.iban), sep="")
                                                    print(end="\n\n")
                                            transferAcc = int(input("Choose An Account To Transfer Balance: "))
                                            delSelect = int(delSelect)
                                            customer.accounts[transferAcc - 1].balance += customer.accounts[delSelect - 1].balance
                                            customer.accounts.remove(customer.accounts[delSelect - 1])
                                            print("Account Deleted!\nPress Enter To Return..")
                                            input()

                                        else:
                                            print("Incorrect Entrance! \nPress Enter To Return..")
                                            input()
                                    else:
                                        print("Please Type A Number!\nPress Enter To Return..")
                                        input()
                            elif selection2 == 'q' or selection2 == 'Q':
                                break

                            else:
                                print("Incorrect Entrance!\nPress Enter To Return..")
                                input()



                    else:
                        print("Incorrect Password!\nPress Enter To Return To Main Menu..")
                        input()

                else:
                    print("Customer Number Couldn't Found!\nPress Enter To Return To Main Menu..")
                    input()




        elif selection == '2':
            name = input("Name: ")
            splittedName = name.split(" ")
            custNum = input("Customer Number: ")
            print("\n\n*Password Must Contain At Least 1 Uppercase Letter, 1 Lowercase Letter And 1 Number*")
            flag = True

            while flag:
                password = str(input("Password: "))
                upperCounter = 0
                lowerCounter = 0
                numCounter = 0
                symCounter = 0
                nameContainFlag = False

                for i in range(len(splittedName)):
                    if splittedName[i].lower() in password.lower():
                        nameContainFlag = True
                for letter in password:


                    if ord(letter) >= 97 and ord(letter) <= 122:
                        lowerCounter += 1
                    if ord(letter) >= 65 and ord(letter) <= 90:
                        upperCounter += 1
                    if ord(letter) >= 48 and ord(letter) <= 57:
                        numCounter += 1
                    if (ord(letter) >= 32 and ord(letter) <= 47) or (ord(letter) >= 58 and ord(letter) <= 65):
                        symCounter += 1
                if nameContainFlag:
                    print("Password Can't Contain Your Name!")
                    input()

                elif len(password) < 4:
                    print("Password Must Be Longer Than 4 Characters..\nPress Enter To Return..")
                    input()

                elif upperCounter < 1:
                    print("Password Must Contain At Least 1 Uppercase Letter!\nPress Enter To Return..")
                    input()

                elif lowerCounter < 1:
                    print("Password Must Contain At Least 1 Lowercase Letter!\nPress Enter To Return..")
                    input()

                elif numCounter < 1:
                    print("Password Must Contain At Least 1 Number!\nPress Enter To Return..")
                    input()

                elif symCounter < 1:
                    print("Password Must Contain At Least 1 Symbol!\nPress Enter To Return..")
                    input()

                else:
                    users.append(User(name, custNum, password))
                    flag = False
                    print("Registration Completed!\nPress enter to return to main menu..")
                    input()


        elif selection == 'q' or selection == 'Q':
            print("Exitted..")
            quit()




















