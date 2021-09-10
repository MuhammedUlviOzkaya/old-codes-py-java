import sqlite3

con = sqlite3.connect("library.db")

cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    con.commit()

def add_content():
    cursor.execute("Insert into kitaplık Values('Çiçeklerde Bir Telaş Var', 'No.1', 'Neo1Negatif', 198)")
    con.commit()

def add_content2(isim, yazar, yayinevi, sayfa_sayisi):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)", (isim, yazar, yayinevi, sayfa_sayisi))
    con.commit()

def pull_content():
    cursor.execute("Select * from kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def pull_content2():
    cursor.execute("Select İsim, Yazar from kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def pull_content3(yayinevi):
    cursor.execute("Select * from kitaplık where Yayınevi = ?", (yayinevi,))
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def update_content(eski_yayinevi, yeni_yayinevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi = ?", (yeni_yayinevi, eski_yayinevi))
    con.commit()

def delete_content():
    cursor.execute("Delete * from kitaplık")
    con.commit()

delete_content()

con.close()