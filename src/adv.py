from room import Room
from player import Player
import textwrap

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(name="Archibald", current_room="outside", inventory=[])


# Write a loop that:
currently_playing = True

print("Current Room: ", player.room)

while currently_playing is True:
# * Prints the current room name
   
# * Prints the current description (the textwrap module might be useful here).
    #print(room[player.room].description)
# * Waits for user input and decides what to do.
    direction = input("Enter 'n', 'w', 'e', or 's' to traverse, 'q' to quit:  ").lower().strip()
# If the user enters a cardinal direction, attempt to move to the room there.
    try:
        player.set_location(direction)
    except ValueError:
        print("You hit a wall! Try another direction")
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    if direction == "q":
        currently_playing = False