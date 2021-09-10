class Dosya():

    def __init__(self):

        with open("metin.txt", "r", encoding = "utf-8") as file:

            content = file.read()
            words = content.split()
            self.just_words = list()

            for i in words:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                self.just_words.append(i)
            for i in self.just_words:
                print(i)

    def all_words(self):
        words_set = set()

        for i in self.just_words:
            words_set.add(i)

        print("All words....")

        for i in words_set:
            print(i)
            print("****************************************")





dosya = Dosya()

dosya.all_words()