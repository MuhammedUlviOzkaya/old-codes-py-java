import os
import sqlite3

dosya_mevcut = os.path.exists('kitaplik.sqlite')


vt = sqlite3.connect('kitaplik.sqlite')
imlec = vt.cursor()

imlec.execute("SELECT * FROM kitap_bilgisi")
kitaplar = imlec.fetchall()
for i in kitaplar:
    print("Kitap Adı: {}\nYazar Adı: {}\nOkundu Mu: {}".format(i[0], i[1], i[2]))
    print("\n\n")




