# Adventura
Adventura is an open source Python Text Adventure Engine, Not yet uploaded to PyPi (Developer build releasing soon 1-3 days 0.6.2) (due to technical issues to updates and occasions, pypi release delayed sorry for the inconvinience)

Instructions:

# ADD ITEM:
# to add an item name, just use class "item"
# example:
key = Item("key")

===========================================================
# ADD A LOCATION:
# to add a location, use game.add_location
# Example:
game = Game("Enter game title here")
# 
room = Location("Random Room", """Enter description here""")
# 
game.add_location(room)

===========================================================
# INVENTORY:
# to use the inventory, you can make an input that adds an item in a set called inventory

# Example:
game = Game("Enter game title here")
# 
room = Location("Random Room", """Enter description here""")
# 
game.add_location(room)
# 
key = Item("key")
# 
room.add_item(key)
# 
pick_up_key = ItemAction("Take Key", target_item=key)
# 
room.add_activity(pick_up_key)

# that was an example of adding an activity, which will auotomatically add an input in the output which will read the first slot in ItemAction(), which in this situation reads "Take Key". If the player chose that input, it will automatically add a key in the inventory

============================================================
# Transition Action:
# A transition action will make an input go to another room or location, that requires an item to go to the next location, it will check the inventory, if it doesn't have the required item, it wont give the option to leave

# Example
# this is the location
game = Game("Enter game title here")
# 
room = Location("Random Room", """Enter description here""")
# 
game.add_location(room)
# this will add another location for the transition action
roomtwo = Location("Another room", """enter description here""")
# 
game.add_location(roomtwo)
# this will add an item in the location 
key = Item("key")
# 
room.add_item(key)
# here is the item action
pick_up_key = ItemAction("Take Key", target_item=key)
# here is the transition action
open_door = TransitionAction("Open Door", target_location=roomtwo, required_items=key)
# Activities input
room.add_activity(pick_up_key)
# 
room.add_activity(open_door)

# NOTE: IF YOU WISH TO ADD A TRANSITION ACTION WHICH DOESN'T REQUIRE AN ITEM, THE required_item ARGUMENT HAS TO HAVE AN "=None" TO IT
# LIKE THIS: required_items=None
# You can use that argument multiple times to add multiple required items.
==========================================================
# To start the game use game.start()
game.start()

# If the final location is equal to the first, it will end the game with a print action.
