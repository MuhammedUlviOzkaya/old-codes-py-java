import sqlite3

con = sqlite3.connect("test.db")
cursor = con.cursor()
cursor.execute("create table if not exists deneme (Value1, Value2, Value3)")
con.commit()


def new_customer():
    name = input("Name: ")
    customer_number = input("Customer Number: ")
    password = input("Password: ")
    cursor.execute("insert into deneme values(?,?,?)", (name, customer_number, password))
    con.commit()
    print("Registration Completed!\nPress Enter to return to main menu..")
    input()

cursor.execute("update deneme set Value1 = ? where Value1 = ?",("Buz", "Ulvi"))
cursor.execute("update deneme set Value2 = ? where Value2 = ?", ("111", "123"))
con.commit()




cursor.execute("select * from deneme")
value2 = cursor.fetchall()


print(value2)
