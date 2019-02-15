from functions import *

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_info(self):
        new_page(f'You found a {self.name}.\n{self.description}\n')
