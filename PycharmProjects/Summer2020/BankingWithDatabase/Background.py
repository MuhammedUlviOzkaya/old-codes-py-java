import sqlite3

connection_accounts = sqlite3.connect("accounts.db")
cursor_accounts = connection_accounts.cursor()
query = "create table if not exists accounts (CustomerNumber, Balance INT, Iban)"
cursor_accounts.execute(query)
connection_accounts.commit()

connection_users = sqlite3.connect("users.db")
cursor_users = connection_users.cursor()
cursor_users.execute("create table if not exists users (UserName, Customer_Number, Password)")
connection_users.commit()




class User():

    def __init__(self, name, customer_number, password):

        self.name = name
        self.customer_number = customer_number
        self.password = password
        self.accounts = list()



class Account():

    def __init__(self, user:User, balance:int, iban:int):

        self.user = user
        self.balance = balance
        self.iban = iban

def new_customer():
    name = input("Name: ")
    customer_number = input("Customer Number: ")
    password = input("Password: ")
    cursor_users.execute("insert into users values(?,?,?)", (name, customer_number, password))
    sqlite3.connect("users.db").commit()
    print("Registration Completed!\nPress Enter to return to main menu..")
    input()



def disconnect():
    sqlite3.connect("bank.db").close()

def main_menu():
    while True:
        print("""
        [1] - I Am A Customer
        [2] - I Want To Be A Customer
        [Q] - Exit
        
        
        """)
        first_selection = input("Enter Your Selection..")
        if first_selection == "1":

            cursor_users.execute("select * from users")
            users = cursor_users.fetchall()
            while True:
                customer_number = input("Customer Number: ")
                for user in users:
                    if customer_number == user[1]:
                        password = input("Password: ")
                        if password == user[2]:
                            print("WELCOME {}!".format(user[0]))

                            while True:
                                cursor_accounts.execute("select * from accounts where CustomerNumber = ?", (customer_number,))
                                accounts = cursor_accounts.fetchall()
                                print("""
                                [1] - Show Accounts
                                [2] - Create An Account
                                [3] - Delete Account
                                [Q] - Exit
                                
                                """)
                                selection = input("Enter your selection: ")
                                if selection == "1":

                                    if len(accounts) < 1:
                                        print("You don't have an account yet!")
                                        input("Press Enter To Return..")
                                    else:
                                        for i in range(len(accounts)):
                                            print("{}. Account =>\nBalance: {}\nIban: {}".format(i+1, accounts[i][1], accounts[i][2]))
                                            print("\n\n")

                                        chosen = input("Choose An Account Or Return(r): ")
                                        if chosen == "r" or chosen == "R":
                                            pass
                                        elif chosen.isdigit():
                                            if int(chosen) <= len(accounts):
                                                chosen = int(chosen)
                                                iban = accounts[chosen - 1][2]
                                                while True:
                                                    print("""
                                                    [1] - Deposit Money
                                                    [2] - Withdraw Money
                                                    [3] - Send Money
                                                    [Q] - Exit
                                                    
                                                    """)
                                                    operation = input("Choose An Operation..")
                                                    if operation == "1":
                                                        deposit_amount = input("Enter Amount To Deposit: ")
                                                        if deposit_amount.isdigit():
                                                            deposit_amount = int(deposit_amount)
                                                            cursor_accounts.execute("select * from accounts where Iban = ?",(iban,))
                                                            current_balance = int(cursor_accounts.fetchall()[0][1])
                                                            cursor_accounts.execute("update accounts set Balance = ? where Iban = ?", (current_balance + deposit_amount ,iban))
                                                            sqlite3.connect("accounts.db").commit()
                                                            print("Operation Completed!\nNew Balance Is: {}".format(current_balance + deposit_amount))
                                                            input("Press Enter To Return..")
                                                        else:
                                                            print("Amount Must Be Consist Of Numbers!\nPress Enter To Return..")
                                                            input()

                                                    elif operation == "2":
                                                        withdraw_amount = int(input("Enter Amount To Withdraw: "))
                                                        cursor_accounts.execute("select * from accounts where Iban = ?", (iban,))
                                                        current_balance = int(cursor_accounts.fetchall()[0][1])
                                                        if withdraw_amount <= current_balance:
                                                            cursor_accounts.execute("update accounts set Balance = ? where Iban = ?", (current_balance - withdraw_amount, iban))
                                                            sqlite3.connect("accounts.db").commit()
                                                            print("Operation Completed!\nNew Balance Is: {}".format(current_balance - withdraw_amount))
                                                            input("Press Enter To Return..")
                                                        else:
                                                            print("Insufficient Balance!\nPress Enter To Return..")
                                                    elif operation == "3":
                                                        receiver_iban = input("Receiver Account's IBAN: ")
                                                        cursor_accounts.execute("select * from accounts where Iban = ?", (receiver_iban,))
                                                        receiver_account = cursor_accounts.fetchall()
                                                        if len(receiver_account) == 0:
                                                            print("Customer Couldn't Found!\nPress Enter To Return..")
                                                            input()
                                                        else:
                                                            """Receiver account's owner here!"""
                                                            send_amount = int(input("Enter Amount You Want To Send: "))
                                                            cursor_accounts.execute("select * from accounts where Iban = ?", (iban,))
                                                            current_balance = int(cursor_accounts.fetchall()[0][1])
                                                            if send_amount <= current_balance:
                                                                cursor_accounts.execute("update accounts set Balance = ? where Iban = ?", (current_balance - send_amount, iban))
                                                                cursor_accounts.execute("select * from accounts where Iban = ?", (receiver_iban,))
                                                                receiver_current = int(cursor_accounts.fetchall()[0][1])
                                                                cursor_accounts.execute("update accounts set Balance = ? where Iban = ?", (receiver_current + send_amount, receiver_iban ))
                                                                sqlite3.connect("accounts.db").commit()
                                                                print("Sending Completed!\nNew Balance Is: {}".format(current_balance - send_amount))
                                                                input()
                                                            else:
                                                                print("Insufficient Balance!\nPress Enter To Return..")
                                                                input()
                                                    elif operation == "q" or operation == "Q":
                                                        break
                                elif selection == "2":
                                    create_balance = int(input("Enter Balance: "))
                                    create_iban = int(input("Enter IBAN: "))
                                    cursor_accounts.execute("insert into accounts values (?,?,?)",(customer_number, create_balance, create_iban))
                                    sqlite3.connect("accounts.db").commit()
                                    print("Account Created!\nPress Enter To Return..")
                                    input()



                                elif selection == "3":
                                    if len(accounts) <= 1:
                                        print("You Can't Delete Account When You Have Only One!\nPress Enter To Return..")
                                        input()

                                    for i in range(len(accounts)):
                                        print("{}. Account =>\nBalance: {}\nIban: {}".format(i + 1, accounts[i][1], accounts[i][2]))
                                        print("\n\n")

                                    delete = int(input("Choose Account You Want To Delete: "))
                                    if delete <= len(accounts):
                                        deleting = accounts[delete - 1]
                                        deleting_iban = deleting[2]
                                        for i in range(len(accounts)):
                                            print("{}. Account =>\nBalance: {}\nIban: {}".format(i + 1, accounts[i][1], accounts[i][2]))
                                            print("\n\n")

                                        transfer = int(input("Select An Account To Transfer Current Money: "))
                                        if transfer <= len(accounts):
                                            transfer_iban = accounts[transfer - 1][2]
                                            transfer_balance = accounts[transfer - 1][1]
                                            cursor_accounts.execute("update accounts set Balance = ? where Iban = ?", (int(transfer_balance) + int(deleting[1]) ,transfer_iban))
                                            cursor_accounts.execute("delete from accounts where Iban = ?", (deleting_iban, ))
                                            sqlite3.connect("accounts.db").commit()
                                            print("Deleting Completed!\nPress Enter To Return..")
                                            input()
                                        else:
                                            print("There Is No Account Such That!\nPress Enter To Return..")
                                            input()


                                        print("Deleting Completed!\nPress Enter To Return..")
                                    else:
                                        print("There Is Not An Account Such That!\nPress Enter To Return..")
                                        input()

                                elif selection == "q" or selection == "Q":
                                    break








                        else:
                            print("Incorrect Password!")

                    else:
                        print("Customer couldn't found!")
                        input()

        elif first_selection == "2":
            new_customer()

        elif first_selection == "q" or first_selection == "Q":
            exit()


















