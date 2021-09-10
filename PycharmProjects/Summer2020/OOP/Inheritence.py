class Tasit():
    def __init__(self, tekerSayisi, kapiSayisi):
        self.tekerSayisi = tekerSayisi
        self.kapiSayisi = kapiSayisi

    def kapiAc():
        print("Kapı Açıldı")

class Tir(Tasit):
    def __init__(self, tekerSayisi, kapiSayisi, turboSayisi):
        super().__init__(tekerSayisi, kapiSayisi)
        self.turboSayisi = turboSayisi


    def dorseBirak():
        print("Dorse Bırakıldı")



tir = Tir(10,2,20)

print(tir.kapiSayisi)
print(tir.tekerSayisi)