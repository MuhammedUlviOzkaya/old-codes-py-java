import sqlite3
import os

dosya_mevcut = os.path.exists('kitaplik.sqlite')

vt = sqlite3.connect('kitaplik.sqlite')
imlec = vt.cursor()

imlec.execute("DELETE FROM kitap_bilgisi WHERE begeni = ''")
vt.commit()


