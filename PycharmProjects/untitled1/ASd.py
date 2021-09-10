import time
print("Merhaba")
time.sleep(2)
print("Ben Buz")


def faktoriyel(sayi): # buz
    sonuc = 1
    for i in range(1,sayi+1):
        sonuc = sonuc * i
    return sonuc

sayi = 4
print("Sayı faktöriyeli: ",faktoriyel(sayi))










def toplama(x,y):
    return x + y
def ortalama(x,y):
    return toplama(x,y)/2

sayi1 = int(input("Sayı girin: "))
sayi2 = int(input("Sayı girin: "))
print("Sonuç: ",ortalama(sayi1,sayi2))







a = 5
if a == 1 :
    print("A = 1")
elif a == 2:
    print("A = 2 dir")
elif a == 5:
    print("A =5")
else:
    print("Git")

sayı = int(input("Sayı gir:"))

for i in range(2,sayı):
    if sayı & i == 0:
        print("Sayı asal değildir.")











liste = ["Türkiye","Almanya","Rusya"]
for i in liste:
    print(i,end="-")








x = 5
while x > 3:
    print("A")
    x=x-1


while True:
    sayi1 = int(input("Sayı girin:"))
    sayi2 = int(input("Sayı girin:"))
    islem = input("1-Toplama\n2-Çıkarma\n3-Çarpma\nÇıkmak için q tuşlayın")
    if islem =="q":
        continue
    elif islem == "1":
        print(sayi1+sayi2)
    elif islem == "2":
        print(sayi1-sayi2)
    elif islem == "3":
        print(sayi1*sayi2)
    else:
        print("Hata")













vize = int(input("Vize:"))
final = int(input("Final:"))

ortalama = vize * 0.4 + final * 0.6

if final <= 45:
    print("Tebrikler finalde yapamayıp kaldınız")
elif ortalama < 40:
    print("Tebrikler yine kaldınız ama bu kez ortalama ile")
else:
    print("Bravo amk geçtiniz!\n Ortalamanız: ()".format(ortalama))

