# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, location):
        self.location = location

    # def __repr__(self):
    #     if self.location == 'outside':
    #         return f'You are outside of the Cave Entrance.\n{self.location.description}\n\n'
    #     elif self.location == 'overlook':
    #         return f'You are at the {self.location.name}.\n{self.location.description}\n\n'
    #     else:
    #         return f'You are in the {self.location.name}.\n{self.location.description}\n\n'
