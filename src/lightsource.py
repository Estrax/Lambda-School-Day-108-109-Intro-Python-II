from item import Item


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print(
            f'It\'s not wise to drop your source of light!\nYou have dropped out {self.name} here!')
