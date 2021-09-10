import sqlite3
import random
import time
import datetime

con = sqlite3.connect("datas.db")
cursor = con.cursor()

def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 (zaman REAL, tarih TEXT, anahtarKelime TEXT, deger REAL)")

def rastgeleDegerEkle():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarKelime = "Python Sqlite3"
    deger = random.randrange(0, 10)
    cursor.execute("INSERT INTO Tablo1 (zaman, tarih, anahtarKelime, deger) VALUES(?, ?, ?, ?)",(zaman, tarih, anahtarKelime, deger))
    con.commit()

def degerleriAl():
    """cursor.execute("SELECT * FROM Tablo1")"""
    """cursor.execute("SELECT zaman, tarih FROM Tablo1")"""

    """cursor.execute("SELECT * FROM Tablo1 WHERE deger = 0.0")"""
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    for i in data:
        print(i)


def silVeGuncelle():
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("İlk değerler -------------------------------------------")
    for i in data:
        print(i)

    """cursor.execute("UPDATE Tablo1 SET deger = 99 WHERE deger = 0")

    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("Güncellendikten sonra -------------------------------------------")
    for i in data:
        print(i)"""
    cursor.execute("DELETE FROM Tablo1 WHERE deger = 0")
    con.commit()
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("Silme işleminden sonra -------------------------------------------")
    for i in data:
        print(i)

silVeGuncelle()





con.close()
