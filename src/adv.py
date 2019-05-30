from room import Room
from item import Item
from player import Player
from lightsource import LightSource
from treasure import Treasure
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers."""),

    'kitchen': Room("King's Kitchen", """You went in and saw the number of corpses
lying down on the floor next to the fridge.""", True),

    'heap': Room("Notorious Heap", """One of the darkest rooms out there. Are you scared?"""),

    'larger': Room("The Larger Room", """There's a sarcophagus next to the door. What's inside?""", True),
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
room['treasure'].n_to = room['kitchen']
room['kitchen'].s_to = room['treasure']
room['kitchen'].e_to = room['larger']
room['larger'].w_to = room['kitchen']
room['larger'].s_to = room['heap']
room['heap'].n_to = room['larger']

#
# Main
#
hammer = Treasure('hammer', 'Gold. Lost after the Canadian Maple War.')
room['heap'].add_item(hammer)

jewel = Treasure('jewel', 'Crown Jewel of United Kitchen')
room['heap'].add_item(jewel)

sword = Treasure(
    'sword', 'Amber sword. Stolen by Japanese and hidden in the Italy for over 20 years. Worth approximately $75 million.')
room['larger'].add_item(sword)

torch = LightSource('torch', 'A torch in the shape of Lambda')
room['outside'].add_item(torch)

# Make a new player object that is currently in the 'outside' room.
player = Player(input('What\'s your name? '), room['outside'])
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
os.system('clear')
print(player.current_room)
while True:
    print('Use "[action] [param]" to do something, e.g. "go n" to go north. Valid directions: n/s/e/w.\nor just type q to quit.')
    in_action = input('What would you like to do now? ')
    action = in_action.split()
    if len(action) == 0:
        continue
    if action[0] == 'q':
        exit()
    elif action[0] == 'go' and action[1] in ['n', 's', 'e', 'w']:
        player.go(action[1])
        os.system('clear')
        print(player.current_room if
              (player.current_room.is_light or
               len(list(filter(lambda x: isinstance(
                   x, LightSource), player.current_room.items))) > 0
               or len(list(filter(lambda x: isinstance(x, LightSource), player.inventory))) > 0)
              else "It's a pitch black!")
    elif action[0] == 'get' or action[0] == 'take':
        if player.current_room.is_light or len(list(filter(lambda x: isinstance(x, LightSource), player.current_room.items))) > 0 or len(list(filter(lambda x: isinstance(x, LightSource), player.inventory))) > 0:
            player.get_item(action[1])
            continue
        print("Good luck finding that in the dark!")
    elif action[0] == 'drop':
        player.drop_item(action[1])
    elif action[0] == 'i' or action[0] == 'inventory':
        player.print_items()
    else:
        print("Action not allowed!")
    print()
