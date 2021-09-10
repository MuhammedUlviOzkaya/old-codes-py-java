import sqlite3

con = sqlite3.connect("market.db")
cursor = con.cursor()

cursor.execute("create table if not exists Market (ProductName TEXT, Price INT )")
con.commit()

def add_product(productName, price):
    cursor.execute("insert into Market values(?,?)", (productName, price))
    con.commit()

def delete_product(productName):
    cursor.execute("delete from Market where ProductName = ?", (productName, ))
    con.commit()

def show_products():
    cursor.execute("select * from Market")
    products = cursor.fetchall()
    for i in range(len(products)):
        print("{}. Product Name: {}\nPrice: {}\n\n".format(i + 1,products[i][0], products[i][1]))


delete_product("Islak Mendil")
show_products()
