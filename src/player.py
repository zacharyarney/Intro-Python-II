from functions import clear
from animations import *
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, location):
        self.location = location

    def get_location(self):
        slow_animation(walk)
        self.location.get_info()
