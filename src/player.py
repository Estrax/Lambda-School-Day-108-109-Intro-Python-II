# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def go(self, direction):
        if getattr(self.current_room, f'{direction}_to') != None:
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print(
                f'There is no path in that direction! Choose another path, {self.name}')

    def get_item(self, item_name):
        if len(self.current_room.get_item(item_name)) == 0:
            print(f'There is no item called {item_name}!')
            return
        self.inventory.extend(self.current_room.get_item(item_name))
        self.current_room.get_item(item_name)[0].on_take()
        self.current_room.remove_item(item_name)

    def drop_item(self, item_name):
        item = list(filter(lambda x: x.name == item_name, self.inventory))
        if len(item) == 0:
            print(f'There is no item called {item_name}!')
            return
        self.current_room.add_item(item[0])
        item[0].on_drop()
        self.inventory = list(
            filter(lambda x: x.name != item_name, self.inventory))

    def print_items(self):
        print(
            f'{self.name}, here are your items: {str([item.name for item in self.inventory])}')
