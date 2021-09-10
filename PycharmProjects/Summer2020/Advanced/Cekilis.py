import random
import time
isimler = []

while True:
    print("Enter names: \nType q for finish..")
    a = input()
    if a == "q" or a == "Q":
        break
    isimler.append(a)


sayi = random.randint(0, len(isimler) - 1)
sayi2 = random.randint(0, len(isimler) - 1)

while True:
    if sayi == sayi2:
        sayi2 = random.randint(0, len(isimler) - 1)
    else:
        break

print("Çekiliş yapılıyor..")
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)

print(isimler[sayi])
print(isimler[sayi2])


