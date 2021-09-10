import sqlite3

db = sqlite3.connect('kitaplik.sqlite')

imlec = db.cursor()

menu = """
[1] - Kitap Ara 
[2] - Yazar Ara

"""

print(menu)
islem = input("İşleminiz: ")

if islem == "1":
    isim = input("Kitap Adı: ")
    sorgu = "SELECT * FROM kitap_bilgisi where kitapAdi = '{}'".format(isim)
    imlec.execute(sorgu)
    veriler = imlec.fetchall()
    for i in veriler:
        print(i)
if islem == "2":
    yazar = input("Yazar Adı: ")
    sorgu = "SELECT * FROM kitap_bilgisi where yazarAdi = '{}'".format(yazar)
    imlec.execute(sorgu)
    veriler = imlec.fetchall()
    for i in veriler:
        print(i)
