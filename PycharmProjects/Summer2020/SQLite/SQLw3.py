import sqlite3

con = sqlite3.connect("dersler.db")

cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT, soyad TEXT, numara INT, ogrencinotu INT)")
    con.commit()


def degerEkle():
    cursor.execute("INSERT INTO ogrenciler VALUES ('Muhammed Ulvi', 'Özkaya', 17, 100)")
    con.commit()
    con.close()



tabloolustur()
degerEkle()