import random
import time

class Remote():

    def __init__(self, tv_status = "OFF", tv_volume = 0, channel_list = ["BUZ"], channel = "BUZ"):

        self.tv_status = tv_status
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel = channel

    def turn_on(self):

        if self.tv_status == "ON":
            print("TV is already ON")
        else:
            print("TV is turning ON..")
            self.tv_status = "ON"

    def turn_off(self):

        if self.tv_status == "OFF":
            print("TV is already OFF")
        else:
            print("TV is turning OFF..")
            self.tv_status = "OFF"

    def volume_settings(self):
        while True:
            selection = input("Volume Down: '<'\nVolume Up: '>'\nExit: 'q'")

            if selection == "<":
                if self.tv_volume != 0:
                    self.tv_volume -= 1
                    print(self.tv_volume)
            elif selection == ">":
                if self.tv_volume != 32:
                    self.tv_volume += 1
                    print(self.tv_volume)
            else:
                print("Volume Upgraded:", self.tv_volume)
                break

    def add_channel(self, channel_name):
        self.channel_list.append(channel_name)
        print("Channel Added!")

    def delete_channel(self):
        for i in range(len(self.channel_list)):
            print(i + 1,". ", self.channel_list[i], sep="")
        selection = int(input("\nChoose to delete.."))
        self.channel_list.remove(self.channel_list[selection - 1])
        print("Channel is removed.")

    def random_channel(self):

        randomCh = random.randint(0, len(self.channel_list) - 1)
        self.channel = self.channel_list[randomCh]

        print("Current Channel Is: ", self.channel)

    def show_channels(self):
        for i in range(len(self.channel_list)):
            print(i + 1, ". ", self.channel_list[i], sep = "")

    def __len__(self):
        return len(self.channel_list)

    def __str__(self):
        return "TV Status: {}\nTV Volume: {}\nChannel List: {}\nCurrent Channel: {}\n".format(self.tv_status, self.tv_volume, self.channel_list, self.channel)

remote = Remote()



while True:
    print("""
    TV Application

    1. Turn ON TV

    2. Turn OFF TV

    3. Volume Settings

    4. Add Channel

    5. Count of Channels

    6. Go To A Random Channel

    7. TV Info
    
    8. Delete Channel
    
    9. Channel List

    Press q to quit..

    """)
    select = input("Select an operation..")

    if select == "q" or select == "Q":
        print("Exitting..")
        break

    elif select == "1":
        remote.turn_on()
    elif select == "2":
        remote.turn_off()
    elif select == "3":
        remote.volume_settings()
    elif select == "4":
        ch_names = input("Enter channel names by splitting them with \",\"")
        ch_names = ch_names.split(",")

        for add in ch_names:
            remote.add_channel(add.strip())

    elif select == "5":
        print("Count of Channels is: {}".format(len(remote)))
    elif select == "6":
        remote.random_channel()
    elif select == "7":
        print(remote)
    elif select == "8":
        remote.delete_channel()
    elif select == "9":
        remote.show_channels()

    else:
        print("Incorrect Entrance!")
        input()





