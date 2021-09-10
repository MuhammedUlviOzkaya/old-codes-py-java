class Customer():
    def __init__(self, ID, password, name):
        self.ID = ID
        self.password = password
        self.name = name
        self.balance = 0

class Bank():
    def __init__(self):
        self.customers = list()

    def be_A_Customer(self, ID, password, name):
        self.customers.append(Customer(ID, password, name))
        print("Registration Completed!")


def main():
    bank = Bank()
    while True:
        print("""
        [1] - I am a customer.
        [2] - I want to be a customer.
        """)
        selection = input("Enter your selection..")
        if selection == '1':

            for i in bank.customers:
                ids = [i.ID]
            ID = input("ID: ")
            if ID in ids:
                for customer in bank.customers:
                    if ID == customer.ID:

                        print("Welcome! {}".format(customer.name))
                        password = input("Password: ")
                        if password == customer.password:
                            print("Entrance Completed!")
                            while True:
                                print("""
                                [1] - Check Balance 
                                [2] - Deposit Money (To My Account)
                                [3] - Deposit Money (To Another Account)
                                [4] - Withdraw Money
                                [Q] - Exit
                                """)

                                selection2 = input("Enter your selection..")
                                if selection2 == '1':
                                    print("Balance is: {}".format(customer.balance))
                                    input("Press enter to return to main menu..")

                                elif selection2 == '2':
                                    amount = int(input("Enter Amount: "))
                                    confirm = input("Do you confirm to deposit {} TL amount to your account? Y/N\n".format(amount))
                                    if confirm == 'Y' or confirm == 'y':
                                        customer.balance += amount
                                        print("Depositing completed!\nNew balance is: {}".format(customer.balance))
                                        input("Press enter to return to main menu..")
                                    elif confirm == 'N' or confirm == 'n':
                                        print("Operation canceled. ")
                                        input("Press enter to return to main menu..")
                                    else:
                                        print("Faulty entrance!")
                                        input("Press enter to return to main menu..")

                                elif selection2 == '3':
                                    findingID = input("Customer ID: ")
                                    if findingID in ids:
                                        for otherCustomer in bank.customers:
                                            if findingID == otherCustomer.ID:
                                                amount2 = int(input("Enter Amount: "))
                                                if amount2 <= customer.balance:

                                                    confirm2 = input("Do you confirm to send {} TL money to {}'s account? Y/N\n".format(amount2, otherCustomer.name))
                                                    if confirm2 == 'Y' or confirm2 == 'y':
                                                        otherCustomer.balance += amount2
                                                        customer.balance -= amount2

                                                    elif confirm2 == 'N' or confirm2 == 'n':
                                                        print("Operation Cancelled. ")
                                                        input("Press enter to return to main menu..")

                                                    else:
                                                        print("Faulty entrance!")
                                                        input("Press enter to return to main menu..")
                                                else:
                                                    print("Insufficient balance! Operation cancelled!")
                                                    input("Press enter to return to main menu..")
                                    else:
                                        print("Customer couldn't found.")
                                        input("Press enter to return to main menu..")

                                elif selection2 == '4':
                                    wdAmount = int(input("Enter amount: "))
                                    if wdAmount <= customer.balance:
                                        customer.balance -= wdAmount
                                        print("Operation Completed! Pick your money..")
                                        print("New balance is: {}".format(customer.balance))
                                        input("Press enter to return to main menu..")
                                    else:
                                        print("Insufficient balance! Operation cancelled!")
                                        input("Press enter to return to main menu..")

                                elif selection2 == 'Q' or selection2 == 'q':
                                    break
        elif selection == '2':
            ID = input("ID: ")
            NAME = input("Name: ")
            PASSWORD = input("Password: ")
            bank.be_A_Customer(ID,PASSWORD,NAME)
            print("Now you're our customer! Welcome!")
main()