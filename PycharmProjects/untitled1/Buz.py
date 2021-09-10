import time




hesaplar = {
    "Buz":{
        "hesapNo":"12345",
        "bakiye": 5300,
        "sifre": "123"
    },
    "Ahmet":{
        "hesapNo":"54321",
        "bakiye": 7000,
        "sifre": "321"
    }}
def paraCek(kullanici):
        miktar = int(input("Miktar Giriniz:"))
        if hesaplar[kullanici]["bakiye"] < miktar:
            print("Yetersiz Bakiye!")
        else:

            hesaplar[kullanici]["bakiye"] -= miktar
            print("Para Geliyor...")
            time.sleep(1.5)
            print("Paranız Verildi")
            print("Kalan Bakiyeniz: ", hesaplar[kullanici]["bakiye"])

def ParaYatir(kullanici):
        miktar = int(input("Miktar Giriniz:"))
        hesaplar[kullanici][bakiye] += miktar
        print("Paranız Yatırılıyor...")
        time.sleep(2)
        print("Yeni Bakiyeniz: ",hesaplar[kullanici]["bakiye"])

def bakiyeSorgula(kullanici):
    print("{} nolu hesabınızda {} tl bakiye bulunmaktadır.".format(hesaplar[kullanici]["hesapNo"],
            hesaplar[kullanici]["bakiye"]))

kullanici = input("Kullanıcı adı girin:")
sifre = input("Şifre girin: ")
while True:

        if kullanici in hesaplar and sifre == hesaplar[kullanici]["sifre"]:
            print("Hoş Geldiniz!")
            islem = input("1-Para Yatırma\n2-Para Çekme\n3-Bakiye Sorgula\nÇıkış yapmak için \"q\" tuşlayın.")

            if  islem == "1" :
                ParaYatir()
            elif islem == "2":
                paraCek(kullanici)
            elif islem == "3":
                bakiyeSorgula(kullanici)
            elif islem == "q":
                break
            else:
                print("Geçersiz İşlem Girdiniz!")


        elif kullanici in hesaplar and sifre != hesaplar[kullanici]["sifre"]:
            print("Şifre Yanlış!")
            kullanici = input("Kullanıcı Adı Girin:")
            sifre = input("Şifrenizi Girin:")
        else:
            print("Kullanıcı Bulunamadı!")
            kullanici = input("Kullanıcı Adı Girin:")
            sifre = input("Şifrenizi Girin:")















