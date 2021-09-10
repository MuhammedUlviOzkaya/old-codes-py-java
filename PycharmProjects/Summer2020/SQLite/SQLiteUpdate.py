import sqlite3
import os

dosya_mevcut = os.path.exists('kitaplik.sqlite')

vt = sqlite3.connect('kitaplik.sqlite')

imlec = vt.cursor()

imlec.execute("UPDATE kitap_bilgisi SET begeni = '' WHERE okunmaDurumu ='Hayır'")
vt.commit()

imlec.execute("SELECT * FROM kitap_bilgisi")
kitaplar = imlec.fetchall()

for i in kitaplar:
    print("Kitap Adı: {}\nYazar Adı: {}\nOkundu Mu: {}\nBeğeni: {}".format(i[0], i[1], i[2], i[3]))