import sqlite3

veritabani = sqlite3.connect("kitaplik.sqlite")

imlec = veritabani.cursor()

imlec.execute("CREATE TABLE IF NOT EXISTS kitap_bilgisi (kitapAdi, yazarAdi, okunmaDurumu, begeni)")

"""imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Suç Ve Ceza', 'Dostoyevski', 'Evet', '*****')")
imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Beyaz Diş', 'Jack London', 'Evet', '****')")"""
imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Yunan Mitolojisi', 'Anna Ve Louie', 'Hayır', '*****')")


veritabani.commit()

veritabani.close()
