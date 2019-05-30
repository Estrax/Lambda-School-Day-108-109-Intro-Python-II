# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []

    def __str__(self):
        return f'{self.name}\n{textwrap.fill(self.description, width=50)}\n\nPossible directions: {self.get_available_directions()}'

    def get_available_directions(self):
        return list(filter(lambda x: getattr(self, f'{x}_to') != None, ['n', 's', 'e', 'w']))
