import random
import os

words = ["zürafa", "tavuk", "ayı", "kaplan", "köpek", "tırtıl", "yengeç", "kanguru", "ördek", "karpuz", "kavun"]
while True:
    flag = False
    word = words[random.randint(0, len(words) - 1)]
    wordTemp = "_" + " _" * (len(word) - 1)
    trying = len(word) * 2
    gameFlag = False
    letters = list()
    while True:
        os.system("cls")
        print()
        print(wordTemp)
        print("Lives: {}".format(trying))
        entrance = input("Type 1 to guess..\nType q to quit..\nEnter a letter: ")
        entrFlag = False
        if entrance.lower() == "q":
            print("Have a nice day!")
            quit()
        elif entrance == "1":
            guess = input("Enter your guess: ")
            if guess.lower().strip() == word:
                print("\n\n*****CONGRATULATIONS!*****")
                while True:
                    select = input("\nType 1 to play again..\nType 2 to quit..")
                    if select == "1":
                        gameFlag = True
                        break
                    elif select == "2":
                        print("Have a nice day!")
                        quit()
                    else:
                        print("Incorrect Entrance!")
                        input()
            else:
                print("Incorrect Guess!\nThe word was: {}".format(word))
                while True:
                    select = input("\nType 1 to play again..\nType 2 to quit..")
                    if select == "1":
                        gameFlag = True
                        break
                    elif select == "2":
                        print("Have a nice day!")
                        quit()
                    else:
                        os.system("cls")
                        print("Incorrect Entrance!")
                        input()
        else:
            if entrance in letters:
                print("\nYou already used this letter!\nTry another one!\n")
                input()
                continue
            else:
                letters.append(entrance)
                for i in range(len(word)):
                    if entrance.lower().strip() == word[i]:
                        entrFlag = True
                        cont = i * 2
                        wordTemp = wordTemp[:cont] + word[i] + wordTemp[cont + 1:]
                        if "_" not in wordTemp:
                            print("\n\n",wordTemp,sep="")
                            print("\n*****CONGRATULATIONS!*****")
                            while True:
                                select = input("\nType 1 to play again..\nType 2 to quit..")
                                if select == "1":
                                    gameFlag = True
                                    break
                                elif select == "2":
                                    print("Have a nice day!")
                                    quit()
                                else:
                                    os.system("cls")
                                    print("Incorrect Entrance!")
                                    input()

        if entrFlag == False:
            trying -= 1
        if trying == 0:
            os.system("cls")
            print("\n\nGAME OVER!")
            print("The word was: {}".format(word))
            while True:
                select = input("\nType 1 to play again..\nType 2 to quit..")
                if select == "1":
                    gameFlag = True
                    break
                elif select == "2":
                    print("Have a nice day!")
                    quit()
                else:
                    os.system("cls")
                    print("Incorrect Entrance!")
                    input()

        if gameFlag:
            break

