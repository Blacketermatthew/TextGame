from player import Player
from room import *
from item import Item, Furniture, Weapon
from character import Character, Enemy
from rpginfo import RPGInfo

## ------- TO DO LIST -------------- ##
"""
- Create items.  
- Create figure out how to add items to rooms
- Create an inventory or backpack system
- Create stats for characters and items
- Maybe? Have identify distinguish between characters and items 
        (i.e. "identify stranger" vs "identify sword")
- Have stats work almost like skill rolls when trying to identify, fight, etc
- Maybe? Allow for clothing and armor
-
 
 
"""
## --------------------------------- ##



# ### Room Creation ###
# kitchen = Room("Kitchen")
# kitchen.set_description("Your standard kitchen.  It's smaller than you'd like.")

# dining_hall = Room("Dining hall")
# dining_hall.set_description("Where we go to eat.  A table centers the room.  Atop the table is a candle and a few matches.")

# dining_hall_to_ballroom_hallway = Room("Hallway")
# dining_hall_to_ballroom_hallway.set_description("A short, narrow hallway.  At the end, two large doors.")

# ballroom = Room("Ballroom")
# ballroom.set_description("Despite the name, there are very few balls present.  Light orange marble covers the circular dance floor, with white pillars standing along the outer edge.")


# ### Mapping Out the Rooms. ###
# ## link_room() connects one room to another room in the direction of wherever the parameter room is.  Room must first be declared as a Room() object
# kitchen.link_room(dining_hall, "south") ## Makes the dining hall south of the kitchen, just as the next line places and connects it to the north
# dining_hall.link_room(kitchen, "north")
# dining_hall.link_room(dining_hall_to_ballroom_hallway, "west")
# dining_hall_to_ballroom_hallway.link_room(dining_hall, "east")
# dining_hall_to_ballroom_hallway.link_room(ballroom, "west")
# ballroom.link_room(dining_hall_to_ballroom_hallway, "east")


### Creating the Characters and Enemies ###
dave = Character("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

gorgo = Enemy("Gorgo", "A bulbous, gurgling bipedal creature with six bony arms.  Smells like trash.")
gorgo.set_weakness("flaming sword")
ballroom.set_character(gorgo)


### Creating and Placing Items ###
cheese = Item("cheese")
cheese.set_description("A single slice of yellow cheese.  I doubt this will come in handy.")
kitchen.place_item(cheese)

dinner_table = Furniture("dining room table")
dinner_table.set_description("A thick, dark brown wooden table that can seat about 6 people. \
        On the edge near one of the chairs, you see a box of matches and large, yellow candle.")
dining_hall.place_item(dinner_table)

matches = Item("matches")
matches.set_description("A small red and white box containing 4 matches.")
dining_hall.place_item(matches)

keys = Item("keys")
keys.set_description("A bunch of keys held together by a large, rusty keyring.")
dining_hall_to_ballroom_hallway.place_item(keys)





######################################################
################### MAIN GAME ########################
######################################################

### Game Variable Setup ###
current_room = kitchen  ## Where you start off.
player = Player()
inventory = player.inventory  # This is an empty list in Item that will have taken items appended to, so it follows them between rooms.

dead = False  ## Gets turned True once you die
main_game = RPGInfo("Untitled Game")  ## Creates an instance of the title screen
main_game.welcome()  


### Main Game/Command Loop ###


# This baby keeps the game going while you're alive.
while dead == False:
        print("\n===============================================================================\n\n")
        
        current_room.get_details()
        inhabitant = current_room.get_character()
        items_in_room = current_room.get_all_items_in_room()

        if inhabitant is not None:
                inhabitant.describe()

        print("\n\nCommands available: [ Greet | Insult | Identify | Take | Inventory | Fight ]")
        command = (input("> ").lower())
        print("\n\n\n\n===============================================================================\n")


        if command in ["north", "south", "east", "west"]:
                current_room = current_room.move(command)
                print(f"You go {command}.")

        elif command == "greet": 
                if inhabitant is not None:
                        print("[You greet " + inhabitant.name + "]")
                        inhabitant.greet()
                elif inhabitant is None:
                        print("There is nobody here to talk to.")

        elif command == "fight":
                if inhabitant is not None and isinstance(inhabitant, Enemy):
                        fight_with = input("What will you fight with? : ")
                        fight_outcome = inhabitant.fight(fight_with)
                        if fight_outcome == True:
                                current_room.set_character(None)
                        elif fight_outcome == False:
                                print("\nYou have been defeated.  GAME OVER")
                                dead = True
                elif inhabitant is not None and isinstance(inhabitant, Character):
                        print("You should not fight someone who isn't your enemy!")
                elif inhabitant is None:
                        print("There is nobody here to fight.")
                else:
                        print("You are currently unable to fight anybody.")
                
        elif command == "identify":
                if inhabitant is not None:
                        if inhabitant.__class__.__name__ == "Enemy":
                                inhabitant.identify()
                        else:
                                print(f"You are unable to get a read on {inhabitant.name}")                
                                        
                elif inhabitant is None:
                        print("There is nobody here to identify.")

        elif command == "insult":
                if inhabitant is not None:
                        inhabitant.insult_count += 1
                        if inhabitant.insult_count < 3:
                                inhabitant.insult()             
                        elif inhabitant.insult_count >= 3:
                                print(inhabitant.name + ", now angry, is charging towards you.")
                                fight_with = input("What will you fight with? : ")
                                fight_outcome = inhabitant.fight(fight_with)
                                if fight_outcome == True:
                                        current_room.set_character(None)
                                elif fight_outcome == False:
                                        print("\nYou have been defeated.  GAME OVER")
                                        dead = True
                elif inhabitant is None:
                        print("There is nobody here to insult.")

        elif command == "inventory":
                #Item.check_inventory(Item)
                player.check_inventory()

        elif command.startswith("take") is True:
                
                # Holding onto this code for a bit while I make sure its predecessor 
                #for x in items_in_room:  # For checking to see what items are in this room.
                #        print(x.get_name())
                #print(current_room.items_in_room)
                
                # items_in_room_list = {x.get_name() for x in items_in_room}
                # print(items_in_room_list)

                # items_in_room_dict = {}
                # for item in items_in_room:
                #         items_in_room_dict[str(item.get_name())] = item
                
                if items_in_room is not None:
                        item_taken = command[5:]  # This tries to return the text after "take " as an item
                        if item_taken in items_in_room:
                                if items_in_room[item_taken].can_put_in_inventory == True:
                                        print(f"You add {item_taken} to your inventory.") 
                                        inventory.append(item_taken)
                                        # del items_in_room[item_taken]
                                        items_in_room.pop(item_taken)

                                else:
                                        print("You are unable to add that item to your inventory.")

                        elif item_taken in inventory:
                                print("You've already added that to your inventory.")
                        else:
                                print("What would you like to take?")

                elif items_in_room is None:
                        print("There is nothing in the room to take")

        else: 
                print(f"Sorry, I did not understand the command: '{command}'")

