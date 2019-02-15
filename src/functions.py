import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def new_page(msg):
    clear()
    print(msg)


def response(msg):
    clear()
    print(msg)
    time.sleep(1.5)
