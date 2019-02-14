from room import Room
from player import Player
from item import Item
from animations import *
from functions import clear
from functions import input_error

# Declare all the rooms

room = {
    'outside':  Room('Outside The Cave Entrance', 'North of you, the cave mount beckons.', grammar='You are '),

    'foyer':    Room('Foyer', '''Dim light filters in from the south. Dusty
passages run north and east.'''),

    'overlook': Room('Grand Overlook', '''A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.''', grammar='You are at the '),

    'narrow':   Room('Narrow Passage', '''The narrow passage bends here from west
to north. The smell of gold permeates the air.'''),

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


fast_animation(splash)


while True:
    player.get_location()

    user_input = input(f'''Where would you like to go from here?
[N]orth
[S]outh
[E]ast
[W]est
>>> ''').lower()

        input(f'''You are at the {player.location.name}.
{player.location.description}
        
Where would you like to go from here?
[N]orth
[S]outh
[E]ast
[W]est
>>> ''')
    else:
        input(f'''You are in the {player.location.name}.
{player.location.description}
        
Where would you like to go from here?
[N]orth
[S]outh
[E]ast
[W]est
>>> ''')
