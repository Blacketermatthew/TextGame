from player import Player
import room as rm
from item import Item, Furniture, Weapon
import character as char
from character import Character, Enemy
from rpginfo import RPGInfo

## ------- TO DO LIST -------------- ##
"""
- Create stats for characters and items
- Have stats work almost like skill rolls when trying to identify, fight, etc
- Maybe? Allow for clothing and armor

"""
## --------------------------------- ##



### Room Creation ###

### Mapping Out the Rooms. ###

### Creating the Characters and Enemies ###

### Creating and Placing Items ###



###############################################################
################### MAIN GAME #################################
###############################################################

### Game Variable Setup ###
current_room = rm.kitchen  ## Where you start off.
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

        print("\n\nCommands available: [ Greet | Insult | Identify | Fight | Look At | Take | Inventory ]")
        command = (input("> ").lower().rstrip())
        print("\n\n\n\n===============================================================================\n")


        if command in ["north", "south", "east", "west"]:

                current_room = current_room.move(command)

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
                        inhabitant.fight(None)

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

                # If you insult somebody 3+ times, they'll attack you.  
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
                player.check_inventory()

        elif command.startswith("take") is True:

                if items_in_room is not None:
                        item_taken = command[5:]  # This grabs the text after "take " to check l
                        if item_taken in items_in_room:
                                if items_in_room[item_taken].can_put_in_inventory == True:
                                        print(f"You add {item_taken} to your inventory.") 
                                        inventory[item_taken] = items_in_room[item_taken]  #  Adds item to inventory
                                        current_room.remove_item(item_taken)
                                        #items_in_room.pop(item_taken)  # Removes item from that room's dict.
                                else:
                                        print("You are unable to add that item to your inventory.")

                        elif item_taken in inventory:
                                print("You've already added that to your inventory.")
                        else:
                                 print(f"I don't think I see '{item_taken}' in here.  What would you like to take?")

                elif items_in_room is None:
                        print("There is nothing in the room to take")

        elif command.startswith("look at") is True:

                object_looked_at = command[8:]  # Everything after "look at " is grabbed

                # Items are placed in different dicts depending on if they're in your inentory or still in the room.
                # This if else statement prints the descriptions for these items.
                if object_looked_at in items_in_room:
                        current_room.describe_item(object_looked_at)
                        #print(current_room.items_in_room[object_looked_at])   # Will be removed; used for testing.

                elif object_looked_at in inventory:
                        inventory[object_looked_at].get_description()
                        #print(inventory[object_looked_at])  # Will be removed; used for testing.
                else:
                        print("What would you like to look at?")

        else: 
                print(f"Sorry, I did not understand the command: '{command}'")

