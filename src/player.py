# Write a class to hold player information, e.g. what room they are in
# currently.
from room import *

class Player:
    """
    starts outside room. Name, current room, todo: inventory
    """
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.room = current_room
        self.inventory = inventory

    def set_location(self, direction):
        """
        update the location based on input, display error if direction not allowed
        """

        next_room = room[self.room].navigate(direction)
        if next_room != None:
            self.room = next_room
            print(next_room)
        else:
            print("You ran into a wall, try another direction!")
