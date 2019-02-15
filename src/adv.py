from room import Room
from player import Player
from item import Item
from animations import *
from functions import clear
from functions import input_error

# Declare all items
item = {
    'gold': Item('Gold-ish Coin', 'Is that gold? Hard to tell in this light.'),
    'pants': Item('Pair Of Pants', 'Hey, these are actually pretty nice! Dry clean only, though.'),
    'sword': Item('Rusty Sword', '''You could definitely kill something with this.
The question is... Do you have the guts?'''),
    'wallet': Item('Your Wallet', 'Do you remember dropping this?'),
    'bone': Item('Bone', 'This is way to big to be human.'),
    'plastic': Item('Piece Of Plastic', '''Looks like this might be the arm from an action figure...
but it's too chewed up to say for sure.'''),
    'food': Item('Some Food', 'Are you really going to eat that?')
}

# Declare all the rooms
room = {
    'outside':  Room('Outside The Cave Entrance', 'North of you, the cave mount beckons.', grammar='You are '),

    'foyer':    Room('Foyer', '''Dim light filters in from the south. Dusty
passages run north and east.''', items=[item['gold'], item['bone']]),

    'overlook': Room('Grand Overlook', '''A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.''', grammar='You are at the ', items=[item['food'], item['sword'], item['gold']]),

    'narrow':   Room('Narrow Passage', '''The narrow passage bends here from west
to north. The smell of gold permeates the air.''', items=[item['pants'], item['pants'], item['gold'], item['plastic']]),

    'treasure': Room('Treasure Chamber', '''You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.'''),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
directions = ['n', 's', 'e', 'w']
quit_commands = ['q', 'quit']
yes = ['y', 'yes']
no = ['n', 'no']
wrong_way_msg = 'There is nothing over there... You ok?'
bad_input_msg = 'What was that?'


def run():
    while True:
        player.get_location()

        user_input = input(f'''What would you like to do here?
Travel? Pick a direction to walk in:
[N]orth [S]outh [E]ast [W]est

[L]ook for items? A room could contain many items,
but you'll only find them if you look.
>>> ''').lower()

        # Quit game
        if user_input in quit_commands:
            clear()
            quit_input = input("""It's a long way home. Are you sure you want to leave?
[Y]es
[N]o
>>> """).lower()
            if quit_input in yes:
                clear()
                return
            elif quit_input in no:
                pass

        # Travel from room to room
        elif user_input in directions:
            if user_input == 'n':
                if hasattr(player.location, 'n_to'):
                    player.location = player.location.n_to
                else:
                    input_error(wrong_way_msg)
            elif user_input == 's':
                if hasattr(player.location, 's_to'):
                    player.location = player.location.s_to
                else:
                    input_error(wrong_way_msg)
            elif user_input == 'e':
                if hasattr(player.location, 'e_to'):
                    player.location = player.location.e_to
                else:
                    input_error(wrong_way_msg)
            elif user_input == 'w':
                if hasattr(player.location, 'w_to'):
                    player.location = player.location.w_to
                else:
                    input_error(wrong_way_msg)

        else:
            input_error(bad_input_msg)


fast_animation(splash)


run()
