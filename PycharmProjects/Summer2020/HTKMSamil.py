import random
import time
import os

liste = ["Taş", "Kağıt", "Makas"]


def countDown(ind):
    os.system("cls")
    print("{} seçildi..".format(liste[int(ind - 1)]), end="\n\n")
    print(3)
    time.sleep(1)
    os.system("cls")
    print("{} seçildi..".format(liste[int(ind - 1)]), end="\n\n")
    print(2)
    time.sleep(1)
    os.system("cls")
    print("{} seçildi..".format(liste[int(ind - 1)]), end="\n\n")
    print(1)
    time.sleep(1)
    os.system("cls")


while True:
    os.system("cls")
    name = input("İsim: ")
    while True:
        limit = input("Final Kaçta Olsun: ")
        if limit.isdigit() == False or limit.isdigit() == 0:
            print("Yanlış Giriş!")
            input()
        else:
            break
    gamerSkor = 0
    pcSkor = 0
    started = False
    flag = False
    os.system("cls")
    print("\n\n*****OYUN BAŞLADI!*****\n\n")
    while True:
        if started == True:
            os.system("cls")
        else:
            pass
        print("------ SKOR ------")
        started = True
        print(name, gamerSkor, "-", pcSkor, "Robot")
        print("""
        |1| - Taş
        |2| - Kağıt
        |3| - Makas 

        """)
        secim = input()
        if secim == "1":
            pcSecim = "Kağıt"
        elif secim == "2":
            pcSecim = "Makas"
        elif secim == "3":
            pcSecim = "Taş"



        if secim == '1':
            countDown(1)
            if pcSecim == "Taş":

                print("Berabere!")
                input("\n\nDevam Etmek İçin Enter..")

            elif pcSecim == "Kağıt":

                print("Robot: Kağıt\n")
                pcSkor += 1
                print("Round'u kazanan: Robot\n")
                input("\nDevam Etmek İçin Enter..")
            elif pcSecim == "Makas":

                print("Robot: Makas\n")
                gamerSkor += 1
                print("Round'u kazanan:", name)
                input("\n\nDevam Etmek İçin Enter..")
        elif secim == '2':
            countDown(2)
            if pcSecim == "Taş":
                print("Robot: Taş\n")
                gamerSkor += 1
                print("Round'u kazanan:", name)
                input("\n\nDevam Etmek İçin Enter..")
            elif pcSecim == "Kağıt":
                print("Berabere!\n")
                input("Devam Etmek İçin Enter..")
            elif pcSecim == "Makas":
                print("Robot: Makas\n")
                pcSkor += 1
                print("Round'u kazanan: Robot\n")
                input("\nDevam Etmek İçin Enter..")
        elif secim == '3':
            countDown(3)
            if pcSecim == "Taş":
                print("Robot: Taş\n")
                pcSkor += 1
                print("Round'u kazanan: Robot\n")
                input("\nDevam Etmek İçin Enter..")
            elif pcSecim == "Kağıt":
                print("Robot: Kağıt\n")
                gamerSkor += 1
                print("Round'u kazanan:", name)
                input("\n\nDevam Etmek İçin Enter..")
            elif pcSecim == "Makas":
                print("Berabere!\n")
                input("\nDevam Etmek İçin Enter..")
        else:
            os.system("cls")
            print("Yanlış Giriş!")
            input()
        if pcSkor == int(limit):
            os.system("cls")
            print("OYUN BİTTİ!\nKAZANAN: Robot!")
            while True:
                print("""
                |1| - Yeniden Oyna
                |2| - Çıkış

                """)
                sonSecim = input()
                if sonSecim == "1":
                    flag = True
                    break

                elif sonSecim == "2":
                    print("Çıkış Yapıldı..")
                    quit()
                else:
                    os.system("cls")
                    print("Yanlış Giriş!")
                    input()
        if flag == True:
            break

        if gamerSkor == int(limit):
            os.system("cls")
            print("\n\n\n\n\nOYUN BİTTİ!\nKAZANAN:", name)
            while True:
                print("""
                |1| - Yeniden Oyna
                |2| - Çıkış

                """)
                sonSecim = input()
                if sonSecim == "1":
                    flag = True
                    break

                elif sonSecim == "2":
                    os.system("cls")
                    print("Çıkış Yapıldı..")
                    quit()
                else:
                    os.system("cls")
                    print("Yanlış Giriş!")
                    input()
        if flag == True:
            break