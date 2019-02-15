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

    def look(self):
        add = ['a', 'add']
        drop = ['d', 'drop']
        items = self.location.items
        if len(items) < 1:
            del_response('You find nothing.')
        else:
            item = items.pop(0)
            item.get_info()
            item_input = input('''What do you want to do with this?
[A]dd to inventory
[D]rop
>>> ''').lower()
            if item_input in add:
                del_response(f'{item.name} added to inventory.')
                self.add_item(item)
            elif item_input in drop:
                del_response("Welp. Don't need that.")
                items.append(item)
            else:
                del_response("You can't do that with this item.")
                items.insert(0, item)
                self.look()