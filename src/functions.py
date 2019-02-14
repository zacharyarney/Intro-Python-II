import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def input_error(msg):
    clear()
    print(msg)
    time.sleep(2)
