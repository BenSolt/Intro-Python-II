from room import Room
from player import Player
# import textwrap
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("OUTSIDE CAVE ENTRANCE",
                     "NORTH of you, the cave mouth beckons"),

    'foyer':    Room("FOYER", """Dim light filters in from the SOUTH. Dusty
passages run NORTH and EAST."""),

    'overlook': Room("GRAND OVERLOOK", """A steep cliff appears before you, falling
into the darkness. Ahead to the NORTH, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("NARROW PASSAGE", """The narrow passage bends here from WEST
to NORTH. The smell of gold permeates the air."""),

    'treasure': Room("TREASURE CHAMBER", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the SOUTH."""),
}

#ITEMS

item = {
    'Item1': Item ('ItemName', ''),
    'Item2': Item ('ItemName', ''),
    'Item3': Item ('ItemName', ''),
    'Item4': Item ('ItemName', ''),
    'Item5': Item ('ItemName', ''),
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

# ADD ITEM TO ROOM
room['outside'].item =[item['Item1']]
room['foyer'].item =[item['Item2']]
room['overlook'].item =[item['Item3']]
room['narrow'].item =[item['Item4']]
room['treasure'].item =[item['Item5']]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

user_name = input("Adventure Game! Enter your players name: ")
player = Player(user_name, room['outside'])
print("player name:", player)

directions = ['n','e','s','w']

# Write a loop that:

while True:
    #move was cmd
    move = input(f"choose direction to walk -> ").split(' ')

    print(f"you have chosen to {move} ")

    if move[0] == 'n':
        if player.location.n_to != None:
            player.location = player.location.n_to
        else:
            print(f"cant go north.")
    elif move[0] == 'e':
        if player.location.e_to != None:
            player.location = player.location.e_to
        else:
            print(f"cant go East.")
    elif move[0] == 's':
        if player.location.s_to != None:
            player.location = player.location.s_to
        else:
            print(f"cant go South.")        
    elif move[0] == 'w':
        if player.location.w_to != None:
            player.location = player.location.w_to
        else:
            print(f"cant go West.")  

    elif move[0] == 'q':
        print('Player quit the game!, Thank you for playing')
        # print(f"Player '{player.name}' quit the game! Thank you for playing")
        
    elif move[0]== 'inv':
        if len(player.items) > 0:
            for item in player.items:
                print(f"you are currently holding {item}")
        else:
            print('your bag is empty')
            

    elif move[0] == 'pickup':
        try: 
            player.pickup_item(move[1])
        except:
            print(f"Enter an item to pickup")
            
    elif move[0] == 'drop':
        try: 
            player.drop_item(move[1])
        except:
            print(f"Select an item to drop")

    elif move[0] == 'look':
        for item in player.location.item:
            print(f"you notice the {item} lying on the ground")
            


        break
    else:
        print(f"invalid entry, n, e, s, w, q,")


   
        
        

# * Prints the current room name

    print(f"you are currently situated in the {player.location}")

# * Prints the current description (the textwrap module might be useful here).

    # print(textwrap.wrap(player.location.description))


# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
