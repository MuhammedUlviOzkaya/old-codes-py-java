import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    con.commit()

def add_content():
    cursor.execute("insert into kitaplık values ('Çiçeklerde Bir Telaş Var', 'Neo1', '258Altkat', 317)")
    con.commit()

def add_content2(isim, yazar, yayinevi, sayfa_sayisi):
    cursor.execute("insert into kitaplık values (?,?,?,?)", (isim, yazar, yayinevi, sayfa_sayisi))
    con.commit()

def pull_content():
    cursor.execute("select * from kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def pull_content2():
    cursor.execute("select İsim, Yazar from kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def pull_content3(yayinevi):
    cursor.execute("select * from kitaplık where Yayınevi = ?", (yayinevi,))
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def update_content(eski_yayinevi, yeni_yayinevi):
    cursor.execute("update kitaplık set Yayınevi = ? where Yayınevi = ?", (yeni_yayinevi, eski_yayinevi))
    con.commit()

def delete_content(yazar):
    cursor.execute("delete from kitaplık where Yazar = ?", (yazar,))
    con.commit()

delete_content("Gazapizm")
pull_content()

con.close()






