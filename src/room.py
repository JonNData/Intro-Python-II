# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    """
    Display the  room and potentially the items
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.s_to = 1
        self.n_to = 1
        self.e_to = 1
        self.w_to = 1

    def navigate(self, direction):
        """
        take the input and turn it into the room direction attribute
        """
        if direction == 'n':
            return self.n_to
        
        elif direction == 's':
            return self.s_to

        elif direction == 'w':
            return self.w_to
        
        elif direction == 'e':
            return self.e_to
        else:
            return None

    def __str__(self):
        return f"\n \n{self.name} : \n {self.description}"

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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