import sqlite3


"""veriler = [('Ahmet Ümit', 'İstanbul Hatırası'),
           ('Yaşar Kemal', 'İnce Memed'),
           ('Paulo Coelho', 'Aldatmak'),
           ('Paulo Coelho', 'Simyacı')]"""

"""imlec.execute("CREATE TABLE if not exists 'kitaplik tablosu' (yazar, kitap)")

for veri in veriler:
    imlec.execute("INSERT INTO 'kitaplik tablosu' VALUES (?, ?)", veri)



db.commit()"""

db = sqlite3.connect("books.sqlite")

imlec = db.cursor()
"""imlec.execute("SELECT * FROM 'kitaplik tablosu'")"""

imlec.execute("SELECT * FROM 'kitaplik tablosu' WHERE yazar = 'Paulo Coelho'")

"""veriler = imlec.fetchall()
for veri in veriler:
    print(veri)"""

"""print(imlec.fetchone())
print(imlec.fetchone())
print(imlec.fetchone())
print(imlec.fetchone())"""

veriler = imlec.fetchmany(5)
for veri in veriler:
    print(veri)

db.close()