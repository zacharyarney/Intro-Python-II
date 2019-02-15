# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, grammar='You are in the ', items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.grammar = grammar

        # # directions
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None

    def get_info(self):
        print(f'{self.grammar}{self.name}.\n{self.description}\n')

    # def __str__(self):
    #     return f'{self.name}'

    # def set_room(self, room, direction):
    #     self[direction.lower()] = room
