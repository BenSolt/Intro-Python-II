from room import Room
from player import Player
from item import Item

# import textwrap

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
    'corpse': Item ('corpse', 'It has been dead for a while. Type -> inspect'),
    'Item2': Item ('ItemName2', ''),
    'Item3': Item ('ItemName3', ''),
    'Item4': Item ('ItemName4', ''),
    'nothing': Item ('ItemName5', ''),
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
room['outside'].item =[item['corpse']]
room['foyer'].item =[item['Item2']]
room['overlook'].item =[item['Item3']]
room['narrow'].item =[item['Item4']]
room['treasure'].item =[item['nothing']]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

user_name = input("Adventure Game!\n Type --> info <-- for Game Menu.\n Enter your players name: ")
player = Player(user_name, room['outside'])
print("player name:", player, )


move = ['n','e','s','w']


# Write a loop that:

while True:
    
    cmd = input(f"choose direction to walk -> ").split(' ')

    print(f"you have chosen to walk {cmd} ")

    if cmd[0] == 'n':
        if player.location.n_to != None:
            player.location = player.location.n_to
        else:
            print(f"cant go north.")        
            
    elif cmd[0] == 'e':
        if player.location.e_to != None:
            player.location = player.location.e_to
        else:
            print(f"cant go East.")
    elif cmd[0] == 's':
        if player.location.s_to != None:
            player.location = player.location.s_to
        else:
            print(f"cant go South.")        
    elif cmd[0] == 'w':
        if player.location.w_to != None:
            player.location = player.location.w_to
        else:
            print(f"cant go West.")  
            
# # QUIT GAME
#     elif cmd[0] == 'q':
#         print('Player quit the game!, Thank you for playing')
#         # print(f"Player '{player.name}' quit the game! Thank you for playing")
#         break
# ITEMS
    elif cmd[0]== 'I':
        if len(player.items) > 0:
            for item in player.items:
                print(f"you are currently holding {item}")
        else:
            print('your bag is empty')
            
#PICKUP ITEM
    elif cmd[0] == 'pickup':
        try: 
            player.pickup_item(cmd[1])
        except:
            print(f"Enter an item to pickup")
            
#DROP ITEM           
    elif cmd[0] == 'drop':
        try: 
            player.drop_item(cmd[1])
        except:
            print(f"Select an item to drop")
            
#LOOK AROUND ROOM
    elif cmd[0] == 'look':
        for item in player.location.item:
            print(f"you notice the {item}")
            
    elif cmd[0] == 'inspect':
        for item in player.location.item:
            print(f"you inspect {item} and find...")
            
# GAME INFO            
    elif cmd[0] == 'info':
        print(f"GAME INFO\n type -> move = n, e, s, w\n type -> i = Inventory\n type -> look = look for items to pickup\n type -> inspect = inspect item\n pickup = pickup Item\n type -> drop = drop Item\n  type -> q = Quit\n")
            
    
    else:
        print(f"invalid entry, n, e, s, w, q, look, pickup")
        
# QUIT GAME
    if cmd[0] == 'q':
        print('Player quit the game!, Thank you for playing')
        # print(f"Player '{player.name}' quit the game! Thank you for playing")
        break

   
        
        

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
