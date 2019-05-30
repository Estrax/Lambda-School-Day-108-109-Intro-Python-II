from item import Item


class Treasure(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
