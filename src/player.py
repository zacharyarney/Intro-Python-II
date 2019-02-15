from functions import *
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, location, inventory=[]):
        self.location = location
        self.inventory = inventory

    def get_location(self):
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

    def add_item(self, item):
        self.inventory.append(item)

    def get_inventory(self):
        back = ['b', 'back']
        new_page('Inventory:')
        if len(self.inventory) < 1:
            print('You have nothing. Even your wallet is missing.\nHow did you lose that?')
        else:
            for i, item in enumerate(self.inventory):
                print(f'{i + 1} - {item.name}')
                
        inv_input = input('\n[B]ack [U]se\n>>> ').lower()
        if inv_input in back:
            self.get_location()
        else:
            del_response('Huh?')
            self.get_inventory()
