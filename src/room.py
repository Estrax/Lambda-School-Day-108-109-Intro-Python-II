# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap


class Room:
    def __init__(self, name, description, is_light=False):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []
        self.is_light = is_light

    def __str__(self):
        return f'{self.name}\n{textwrap.fill(self.description, width=50)}\n\nItems in this room: {self.get_items_list()}\n\nPossible directions: {self.get_available_directions()}'

    def get_available_directions(self):
        return list(filter(lambda x: getattr(self, f'{x}_to') != None, ['n', 's', 'e', 'w']))

    def get_items_list(self):
        return str([item.name for item in self.items])

    def get_item(self, item_name):
        return list(filter(lambda x: x.name == item_name, self.items))

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = list(filter(lambda x: x.name != item_name, self.items))
